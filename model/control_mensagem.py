import datetime

from data.conexao import Conexao


class Mensagem:

    def cadastrar_mensagem(usuario, comentarios):
        data_hora = datetime.datetime.today()

        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor()

        sql = """   INSERT INTO tb_comentarios (nome, data_hora, comentario) VALUES (%s, %s, %s)"""

        valores = (usuario, data_hora, comentarios )

        cursor.execute(sql, valores)

        conexao.commit()

        cursor.close()

        conexao.close()

    def mostra_mensagens():
        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor(dictionary=True)

        sql = """   SELECT nome as usuario, comentario, data_hora, cod_comentario from tb_comentarios"""

        cursor.execute(sql)

        resultado = cursor.fetchall()

        cursor.close()

        conexao.close()

        return resultado
    
    def excluir_mensagen(codigo):
        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor()

        sql = """  DELETE from tb_comentarios WHERE cod_comentario =  %s;"""
        valores = (codigo,)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()

    def curtir_comentario(like):
        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor()

        sql = """ SELECT curtidas from tb_comentarios WHERE cod_comentario = %s;"""

        valores = (like,)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()
    


