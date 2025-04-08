import datetime
from hashlib import sha256

from flask import session
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


        # CRIPTOGRAFANDO SENHA
        senha = sha256(senha.encode()).hexdigest()

        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor(dictionary = True)

        sql = """SELECT login, nome FROM tb_usuarios WHERE login = %s and binary senha = %s;"""

        valores = (login, senha)
        cursor.execute(sql, valores)
        resultado = cursor.fetchone()

        cursor.close()
        conexao.close()
         
        if resultado:
            session['usuario'] = resultado['login']
            session['nome_usuario'] = resultado['nome']
            return True 
        else:
            return False
    
    def logoff():
        session.clear()
            
        