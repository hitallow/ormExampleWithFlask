from app import db 

""""
    Menu de tabelas

""""

class User(db.Model):
    # Nome da minha tabela
    __tablename__ = 'users'

    # campos
    id = db.Column(db.Integer, primary_key=True, unique= True)
    name = db.Column(db.String(30), unique=True, require=True)
    fone = db.Column(db.String)
    createat = db.Column(db.DateTime) 
    description = db.Column(db.Text)

    def __init__(self, name ):
        self.name = name

    def __repr__(self):
        return "<User : {}>".format(self.name)

"""
    Classe(tabela)
"""
class Dependent(db.Model):
    # Nome da minha tabela 
    __tablename__  = 'dependents'

    # campos
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, required = True)
    
        #Exemplo de relacionamento
    user_id = db.Column(db.Integer, db.ForengKey('users.id'))
    user = db.relationship('User', foreing_keys=user_id)

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return "< Dependent : {}>".format(self.name)