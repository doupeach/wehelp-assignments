from crypt import methods
from urllib import response
from flask import Flask,render_template,request,redirect,session,jsonify
import json
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")

db = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  password = PASSWORD,
  database = DATABASE,
  )
cursor=db.cursor(buffered=True)

app=Flask(
    __name__,
    static_folder='static',
    static_url_path='/static')

app.secret_key='asbs'

@app.route('/')
def index():
    session['isLogin'] = '!isLogin'
    return render_template('index.html')

@app.route('/signup',methods=['POST'])
def signup():
    name = request.form['name']
    id = request.form['id']
    pw = request.form['pw']
    sql = "SELECT username from member WHERE username = %s"
    val = (id, )
    cursor.execute(sql, val)
    usernamecheck = cursor.fetchone()

    if len(name) == 0 or len(id) == 0 or len(pw) == 0:
        errorMessage="請輸入姓名、帳號、密碼"
        return redirect('/error/?message='+errorMessage)
    elif usernamecheck:
        errorMessage="帳號已經被註冊"
        return redirect('/error/?message='+errorMessage)
    else:
        sql_insert = "INSERT INTO member(name, username, password) VALUES (%s, %s, %s)"
        val_insert = (name, id, pw)
        cursor.execute(sql_insert, val_insert)
        db.commit()
        return redirect('/')

@app.route('/signin',methods=['POST'])
def signin():
    id = request.form['id']
    pw = request.form['pw']

    sql = "SELECT name, username, password FROM member WHERE username = %s AND password = %s"
    val = (id, pw)
    cursor.execute(sql, val)
    signincheck = cursor.fetchone()

    name = signincheck[0]
    username = signincheck[1]
    

    if id == '' or pw == '':
            errorMessage = '請輸入帳號、密碼'
            return redirect('/error/?message='+errorMessage)
    elif signincheck:
            nameSelect = "SELECT name, username FROM member WHERE username = %s AND password = %s"
            cursor.execute(nameSelect, val)
            session['memberName'] = name
            session['username'] = username
            session['isLogin'] = 'isLogin'
            return redirect("/member")
    else:
        errorMessage = '帳號或密碼輸入錯誤'
        return redirect('/error/?message='+errorMessage)

@app.route('/signout')
def signout():
    session['isLogin'] = '!isLogin'
    return redirect('/')

@app.route('/member/')
def member():
    isLogin = session['isLogin']
    memberName = session['memberName']
    if isLogin != 'isLogin':
        return redirect('/')
    else:
        return render_template('member.html',memberName=memberName)

@app.route('/error/')
def error():
    errorMessage = request.args.get('message',None)
    return render_template('error.html',errorMessage=errorMessage)

# week-7 assignment
@app.route('/api/members',methods=['GET'])
def members():
        username = request.args.get('username')

        if username:
            sql = "SELECT id, name, username FROM member WHERE username = %s"
            val = (username,)
            cursor.execute(sql, val)
            memberCheck = cursor.fetchone()

            if memberCheck:
                dataToJson = {
                    "data":{
                        "id":memberCheck[0],
                        "name":memberCheck[1],
                        "username":memberCheck[2]
                    }
                }
                data = jsonify(dataToJson)
                return data

            else:
                dataToJson = {
                    "data":None
                }
                data = jsonify(dataToJson)
                return data            

@app.route('/api/member', methods=['POST'])
def updateName():
    name = json.loads(request.get_data())["name"]
    if (name == '') or (session['isLogin'] != 'isLogin'):
        return jsonify({"error":True})
    else:
        username = session.get('username')
        session["memberName"] = name
        sql = "UPDATE member SET name = %s WHERE username = %s"
        value = (name, username)
        cursor.execute(sql, value)
        db.commit()

        return jsonify({"ok":True})




app.run(port=3000)