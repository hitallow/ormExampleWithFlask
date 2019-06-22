from flask import Flask

" Instância do aplicativo "
app = Flask(__name__)

" Faço a importação do meu menu de controles"

from app.controllers import urls