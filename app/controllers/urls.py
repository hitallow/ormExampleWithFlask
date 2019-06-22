from app import app

"""
    Rota inicial
"""
@app.route("/")
def hello():
    return "Estou testando"
