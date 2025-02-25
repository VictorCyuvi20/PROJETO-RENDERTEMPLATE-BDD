from flask import Flask, render_template, request, redirect
import datetime
import mysql.connector

app = Flask(__name__)

@app.route("/")
def pagina_principal():
    return render_template("index.html")


@app.route("/post/cadastra_comentario", methods = ["POST"])
def pagina_comentario():
    usuario = request.form.get("usuario")
    comentarios = request.form.get("comentario")
    data_hora = datetime.datetime.today()
    conexao = mysql.connector.connect(host = "localhost", port = 3306, user = "root", password = "root", database = "db_comentarios_pantheon" )
    cursor = conexao.cursor()
    sql = """   INSERT INTO tb_comentarios_pantheon (data_e_hora, nome, comentario) VALUES (%s, %s, %s)"""
    valores = (data_hora, usuario, comentarios )
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect("/")


app.run(debug=True)