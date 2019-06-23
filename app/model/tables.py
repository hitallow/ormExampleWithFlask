from app import db 


#    Menu de tabelas


class User(db.Model):
    # Nome da minha tabela
    __tablename__ = 'users'

    # campos
    id = db.Column(db.Integer, primary_key=True, unique= True)
    name = db.Column(db.String(30), unique=True)
    fone = db.Column(db.String(15))
    createat = db.Column(db.DateTime) 
    description = db.Column(db.Text)

    dependents = db.relationship('Dependent')

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
    name = db.Column(db.String(10))
    
        #Exemplo de relacionamento
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='dependents')


    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return "< Dependent : {}>".format(self.name)

db.create_all()
db.session.commit()