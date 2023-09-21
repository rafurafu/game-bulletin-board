from sqlalchemy.orm import sessionmaker
from db import engine
from model import login
from sqlalchemy import text


SessionClass = sessionmaker(engine)  # セッションを作るクラスを作成
session = SessionClass()
connection = engine.connect()

def selectAllLogin():
    users = session.query(login).all()
    return users

def getLoginUser(username, password):
    query = text(f'SELECT * FROM login WHERE name = "{username}" AND password="{password}"')
    result = connection.execute(query)
    row = result.fetchall()
    return row