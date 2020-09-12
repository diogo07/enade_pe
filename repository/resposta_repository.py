
class RespostaRepository:

    def __init__(self, connection):
        self.connection = connection

    def insert(self, resposta):
        mycursor = self.connection.cursor()
        sql = "INSERT INTO resposta (codigo_questao, id_enade, opcao) VALUES (%s, %s, %s)"
        vals = (resposta.getValues())
        mycursor.execute(sql, vals)
        self.connection.commit()
        return resposta

    def insertMultipleRows(self, sql, dados):
        mycursor = self.connection.cursor()
        try:
            mycursor.executemany(sql, dados)
            self.connection.commit()
        except Exception as e:
            print(e)
