from flask import Flask, render_template, request, redirect
import datetime
import mysql.connector
from data.conexao import Conexao
from model.control_mensagem import Mensagem

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


app.run(debug=True)