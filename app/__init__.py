from flask import Flask

# configurações de bd
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


" Instância do aplicativo "
app = Flask(__name__)
app.config.from_object('config')

"   Configuração de database"



db = SQLAlchemy(app=app)

# crio uma variavel capaz de cuidar das migrações
migrate = Migrate(app=app, db=db)

# este manager cuida da informações de migrações
manager = Manager(app)
manager.add_command('db', MigrateCommand)


db = SQLAlchemy(app=app)

" Faço a importação do meu menu de controles"

from app.controllers import urls