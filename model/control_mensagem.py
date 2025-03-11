import datetime

from data.conexao import Conexao


class Mensagem:

    def cadastrar_mensagem(usuario, comentarios):
        data_hora = datetime.datetime.today()

        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor()

        sql = """   INSERT INTO tb_comentarios_pantheon (data_e_hora, nome, comentario) VALUES (%s, %s, %s)"""

        valores = (data_hora, usuario, comentarios )

        cursor.execute(sql, valores)

        conexao.commit()

        cursor.close()

        conexao.close()

    def mostra_mensagens():
        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor(dictionary=True)

        sql = """   SELECT nome as usuario, comentario, data_e_hora from tb_comentarios_pantheon """

        cursor.execute(sql)

        resultado = cursor.fetchall()

        cursor.close()

        conexao.close()

        return resultado
    


