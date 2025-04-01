import datetime
from hashlib import sha256
from data.conexao import Conexao


class Usuario:
    def cadastro_usuario(login, nome, senha):
        
        senha = sha256(senha.encode()).hexdigest()

        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor()

        sql = """ INSERT INTO tb_usuarios (login, nome, senha) VALUES (%s, %s, %s);"""

        valores = (login, nome, senha)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()



    def login_usuario(login, senha):
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor()

        sql = """SELECT login, senha FROM tb_usuarios WHERE login = %s and binary senha = %s;"""

        valores = (login, senha)
        cursor.execute(sql, valores)
        resultado = cursor.fetchone
        if resultado 
        cursor.close()
        conexao.close()