from app import app, db
from flask import render_template
from flask import request, jsonify
import json
from app.model.tables import User, Dependent 

"""
    Rota inicial
"""
@app.route('/index',  methods=['GET'])
@app.route('/', methods=['GET'] )
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
    response = {
        'id' : user.id
    }

    return json.dumps(response)

@app.route('/index/search', methods=['POST'])
def search():
    users = User.query.order_by(User.name).all()
    return jsonify(list(map(lambda x: x.serialize(), users)))

@app.route('/index/delete', methods=['POST'])
def delete():
    data = request.get_json()
    user = User.query.filter_by(id=data['id']).first()
    db.session.delete(user) 
    db.session.commit()
    return 'OK'


@app.route('/getall')
def getAll():
    pass