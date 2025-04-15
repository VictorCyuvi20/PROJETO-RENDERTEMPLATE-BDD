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

        sql = """SELECT nome as usuario, comentario, data_hora, cod_comentario, curtidas from tb_comentarios"""

        cursor.execute(sql)
        
        # conexao.commit()

        resultado = cursor.fetchall()

        cursor.close()

        conexao.close()

        return resultado
    def last_mensage(usuario):
        
        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor(dictionary=True)

        sql = """SELECT comentario from tb_comentarios where comentario =  %s ORDER BY comentario DESC """

        valores = (usuario,)

        cursor.execute(sql, valores)


        resultado = cursor.fetchone()
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

    def curtir_comentario(codigo):
            conexao = Conexao.criar_conexao()

            cursor = conexao.cursor()

            sql = """ UPDATE tb_comentarios SET curtidas = curtidas + 1 WHERE cod_comentario = %s;"""

            valores = (codigo,)
            cursor.execute(sql, valores)
            conexao.commit()
            cursor.close()
            conexao.close()
            
    def desgosta_mensagem(codigo):
        conexao = Conexao.criar_conexao()
        
        cursor = conexao.cursor()
        
        sql = """ UPDATE tb_comentarios SET curtidas = curtidas - 1 WHERE cod_comentario = %s;"""
        
        valores =  (codigo,)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()






