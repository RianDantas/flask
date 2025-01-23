from flask import *

app = Flask(__name__)

@app.route("/")
def helo_world():
    titulo = "Gestão de alunos"
    usuarios = [
        {"nome": "Alex", "membro_ativo":True},
        {"nome": "João", "membro_ativo":False}
    ]
    return render_template("index.html", titulo=titulo, usuarios=usuarios)

@app.route("/rotaExtra")
def paginaExtra():
    return """
        <p> Testando HTML</p>
        <h1>Pagina 2</h1>
    """


app.run(debug=True)