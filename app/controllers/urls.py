from flask import render_template, request, jsonify

from app import app, db
from app.model.tables import User

"""
    Rota inicial
"""


@app.route('/index', methods=['GET'])
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/getUser", methods=['GET'])
def getUser():
    data = request.get_json()

    user = User.query.filter_by(id=data['id']).first()
    return jsonify(user.serialize())


@app.route('/index/insertUser', methods=['POST'])
def insertUser():
    data = request.get_json()

    user = User(name=data['name'], email=data['email'], addres=data['address'], fone=data['phone'])

    db.session.add(user)
    db.session.commit()

    response = {'id': user.id}
    return jsonify(response)


@app.route('/index/search', methods=['GET'])
def search():
    data = request.get_json()

    like_name = User.name.like(f"%{data['name']}%")
    users = User.query.filter(like_name).order_by(User.name)

    return jsonify(list(map(lambda x: x.serialize(), users)))


@app.route('/index/delete', methods=['DELETE'])
def delete():
    data = request.get_json()
    user = User.query.filter_by(id=data['id']).first()
    db.session.delete(user)
    db.session.commit()

    return jsonify({'result': f"{user.id} Removed!"})


@app.route('/index/update', methods=['PUT'])
def update():
    data = request.get_json()

    if data['id'] is None:
        return jsonify({'error': 'Need id'})

    user = User.query.filter_by(id=data['id']).first()

    if user is not None:
        for key in data:
            if key in user.__dir__() and key != 'id':
                user.__setattr__(key, data[key])

        db.session.commit()

        result = user.serialize()
    else:
        result = { 'error': 'User not found' }

    return jsonify(result)


@app.route('/getAll', methods=['GET'])
def getAll():
    users = User.query.all()

    return jsonify(list(map(lambda x: x.serialize(), users)))
