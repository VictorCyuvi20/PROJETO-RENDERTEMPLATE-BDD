import datetime
from data.conexao import Conexao


class Usuario:
    def cadastro_usuario(login, nome, senha):
        
        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor()

        sql = """ INSERT INTO tb_usuarios (login, nome, senha) VALUES (%s, %s, %s);"""

        valores = (login, nome, senha)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()