from app import app, db
from flask import render_template

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

@app.route('/insertUser')
def insertUser():
    user = User("Maria")
    db.session.add(user)
    db.session.commit()
    return "<h1>Testando</h1>"

@app.route('/search/',defaults={'name':'all'}, methods=['GET'])
@app.route('/search/<name>', methods=['GET'])
def search(name):
    if name != 'all':
        return 'nome {}'.format(name)
    return 'você não passou nome'