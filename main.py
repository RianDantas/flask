from flask import *

app = Flask(__name__)

# Rota do Home

@app.route("/")
def helo_world():
    titulo = "Gestão de alunos"
    


    return render_template("index.html", titulo=titulo)

# Vaiavel global para cadastro de usuarios
usuarios = []

# Rota para o html de cadastrar usuario
@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


# Rota para salvar os usuarios cadastrados na variavel global

@app.route("/cadastroUsuarios", methods=['POST'])
def cadastroUsuarios():
    global usuarios

    nome = request.form.get("nome")
    login = request.form.get("login")
    senha = request.form.get("senhaUsuario")
    usuarios.append({"nome": nome, "login": login, "senha": senha})
    print(usuarios)
    return  render_template("index.html")
    

# Rota para verificar se o login com usuario e senha estão corretos

@app.route("/verificarLogin", methods=['POST'])
def verificarLogin():
    global usuarios
    nomeUsuario = request.form.get('nomeUsuario')
    senha = request.form.get("senhaUsuario")
    for i in usuarios:
        if i["login"] == nomeUsuario and i["senha"] == senha:
            return render_template("convidados.html")

    return render_template("notFound.html")


@app.route("/recuperarSenha")
def recuperarSenha():
    return render_template("recuperarSenha.html")

@app.route("/recuperacao", methods=['POST'])
def recuperacaoDeSenha():
    nome = request.form.get("nome")
    usuario = request.form.get("usuario")


    for i in usuarios:

        if i["nome"] == nome and i["login"] == usuario:
            print(i["senha"])
            message = "Sua senha é: " + i["senha"]
            return render_template("recuperarSenha.html", message=message)

        else:
            message = "nao existe"
            return render_template("recuperarSenha.html", message = message)

































    

app.run(debug=True)