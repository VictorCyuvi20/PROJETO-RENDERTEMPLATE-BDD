from flask import Flask, render_template, request, redirect
import datetime
import mysql.connector
from data.conexao import Conexao
from model.control_mensagem import Mensagem
from model.cadastro_usuario import Usuario

app = Flask(__name__)

@app.route("/")
def pagina_principal():
    mensagem = Mensagem.mostra_mensagens()
    return render_template("index.html", mensagem = mensagem)


@app.route("/post/cadastra_comentario", methods = ["POST"])
def pagina_comentario():
    usuario = request.form.get("usuario")

    comentarios = request.form.get("comentario")

    Mensagem.cadastrar_mensagem(usuario, comentarios)

    return redirect("/")

@app.route("/delete/mensagem/<codigo>")
def pagina_delete(codigo):
    Mensagem.excluir_mensagen(codigo)
    return redirect("/")

@app.route("/put/like/mensagem/<codigo>")
def pagina_like(codigo):

    Mensagem.curtir_comentario(codigo)
    return redirect("/")

@app.route("/put/deslike/mensagem/<codigo>")
def pagina_deslike(codigo):
    
    Mensagem.desgosta_mensagem(codigo)
    return redirect("/")


@app.route("/cadastro ", methods = ["POST"])
def pagina_cadastra():
    login = request.form.get("login")
    nome = request.form.get("nome")
    senha = request.form.get("senha")
    
    Usuario.cadastro_usuario(login, nome, senha)
    return render_template("",)
    


app.run(debug=True)