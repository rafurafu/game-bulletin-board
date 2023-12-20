from flask import Flask, render_template,request,redirect,session,jsonify
import random as rd
#import session as ss
import json
#from model
from collections import Counter
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)















app.route('/')
def index():
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



@app.route('/')
def login():
    return render_template("login.html")


@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/match')
def match():
    return render_template("match.html")

@app.route('/search')
def search():
    return render_template("search.html")



if __name__ == '__main__':
    app.run()