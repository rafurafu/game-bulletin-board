from flask import Flask, render_template,request,redirect,session,jsonify
import random as rd
import session as ss
import json
from model import login
from collections import Counter
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base


app = Flask(__name__)
app.secret_key = 'your_secret_key'


#ログインシステム
def login_required(func):
    def wrapper(*args, **kwargs):
        if 'email' in session:
            #emailがある場合はhomeに移動
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
    email = request.form["email"]
    password = request.form["password"]
    
    print(f"Email: {email}")
    print(f"Password:{password}")
    #email一時的に保存
    #email = セッション
    if loginCheck(email, password):
        return redirect("/home")

    else:
        return redirect("/")


 #ログイン処理　、ユーザー情報の照合 #mysql
def loginCheck(email, password):
    users = ss.getLoginUser(email, password)
    
    if users[0][1] == email and users[0][2] == password:
        session['email'] = email
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

 #ホーム
@app.route('/home')
@login_required
def home():
    return render_template('home.html')











@app.route('/add_tweet', methods=['POST'])
def add_tweet():
    # フォームから送信されたJSONデータを取得
    data = request.get_json()

    # データを使って何か処理を行う（ここでは例としてコンソールに表示）
    print(f"ユーザー情報: 役割={data['role']}, 人数={data['number']}, ランク={data['rank']}")
    print(f"ツイート: {data['tweetText']}")

    # ここでデータベースなどに保存する処理を追加できます

    return jsonify({'status': 'success'})



@app.route('/match')
def match():
    return render_template("match.html")

@app.route('/search')
def search():
    return render_template("search.html")



if __name__ == '__main__':
    app.run()