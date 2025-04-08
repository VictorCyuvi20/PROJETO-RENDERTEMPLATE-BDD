from flask import Flask, render_template, request, redirect, session
import datetime
import mysql.connector
from data.conexao import Conexao
from model.control_mensagem import Mensagem
from model.cadastro_usuario import Usuario

app = Flask(__name__)

app.secret_key = "CRISTOREI"

# ROTAS 

@app.route("/")
def pagina_principal():
    return render_template("login.html",)

@app.route("/login")
def pagina_loga():
    return render_template("index.html")


@app.route("/post/login", methods = ["POST"])
def post_logar():
    login = request.form.get("login")
    senha = request.form.get("senha")

    if Usuario.login_usuario(login, senha):
        return redirect("/comentarios")
    else:
        return redirect("/login")
    
@app.route("/get/logoff")
def post_logoff():
    Usuario.logoff()
    return redirect("/")

@app.route("/comentarios")
def pagina_coment():
    
    if "usuario" in session:

        mensagem = Mensagem.mostra_mensagens()
        return render_template("index.html", Mensagem = mensagem)
    else:
        return redirect("/login")

@app.route("/post/cadastra_comentario", methods = ["POST"])
def pagina_comentario():
    usuario = request.form.get("usuario")

    comentarios = request.form.get("comentario")

    Mensagem.cadastrar_mensagem(usuario, comentarios)

    return redirect("/comentarios")

@app.route("/delete/mensagem/<codigo>")
def pagina_delete(codigo):
    Mensagem.excluir_mensagen(codigo)
    return redirect("/comentarios")

@app.route("/put/like/mensagem/<codigo>")
def pagina_like(codigo):

    Mensagem.curtir_comentario(codigo)
    return redirect("/comentarios")

@app.route("/put/deslike/mensagem/<codigo>")
def pagina_deslike(codigo):
    
    Mensagem.desgosta_mensagem(codigo)
    return redirect("/comentarios")


@app.route("/cadastro",)
def pagina_cadastro():
    return render_template("pagina-principal.html")
    
@app.route("/post/cadastro", methods = ["POST"])
def pagina_cadastra():
    login = request.form.get("login")
    nome = request.form.get("nome")
    senha = request.form.get("senha")
    
    Usuario.cadastro_usuario(login, nome, senha)
    return redirect("/cadastro")
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)