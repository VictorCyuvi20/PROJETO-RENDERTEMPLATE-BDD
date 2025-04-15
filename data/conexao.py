import mysql.connector

class Conexao:

    def  criar_conexao():

        if False:
            conexao = mysql.connector.connect(host = "bdgodofredo-alexstocco-93db.b.aivencloud.com", 
                                            port = 27974, 
                                            user = "3ds", 
                                            password = "banana", 
                                            database = "db_feedback" )
        else: 
            conexao = mysql.connector.connect(host = "localhost", 
                                            port = 3306, 
                                            user = "3ds", 
                                            password = "banana", 
                                            database = "db_feedback" )
        return conexao