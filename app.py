from flask import Flask, render_template,request,redirect,session,jsonify
import session as ss
import random as rd
import json
from model import product
from collections import Counter

app = Flask(__name__)
app.secret_key = 'your_secret_key'

 #ログインシステム 新規登録
def register():
    username = input("ユーザー名を入力してください: ")
    password = input("パスワードを入力してください: ")

def login_required(func):
    def wrapper(*args, **kwargs):
        if 'username' in ss:
            #ユーザーネームがある場合はhomeに移動
            return func(*args, **kwargs)
        else:
            #ユーザーネームがない場合はログイン画面に移動
            return redirect('/')
    return wrapper

 #ログイン
@app.route('/')
def login():
    return render_template("login.html")

@app.route('/login', methods = ["POST"])
def loginProcess():
    username = request.form["username"]
    password = request.form["password"]
    
    print(f"USername: {username}")
    print(f"Password:{password}")
    #username一時的に保存
    #username = セッション
    if loginCheck(username, password):
        return redirect("/home")

    else:
        return redirect("/")
    
 #ログイン処理　、ユーザー情報の照合 #mysql
def loginCheck(username, password):
    users = ss.getLoginUser(username, password)
    
    if users[0][1] == username and users[0][2] == password:
        session['username'] = username
        session['id'] = users[0][0]
        return True
    else:
        return False

 #ログアウト  
@app.route('/logout')
def logout():
    #ログアウトするときにセッションを消す
    session.clear()
    return redirect('/')

