from app import app, db
from flask import render_template
from flask import request, jsonify
import json
from app.model.tables import User, Dependent 

"""
    Rota inicial
"""
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route("/getUser")
def getUser():
    return 'teste'

@app.route('/index/insertUser', methods=['POST'])
@app.route('/index/insertuser', methods=['POST'])
def insertUser():
    data = request.get_json()
    user = User(name=data['name'],email=data['email'], addres=data['address'], fone=data['phone'])
    db.session.add(user)
    db.session.commit()
    return "OK"

@app.route('/search/',defaults={'name':'all'}, methods=['GET'])
@app.route('/search/<name>', methods=['GET'])
def search(name):
    if name == 'all':
        x = User.query.order_by(User.name).all()
    print(x)
    return 'OK'

@app.route('/getall')
def getAll():
    pass