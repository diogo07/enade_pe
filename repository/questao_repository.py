
class QuestaoRepository:

    def __init__(self, connection):
        self.connection = connection

    def insert(self, questao):
        mycursor = self.connection.cursor()
        sql = "INSERT INTO questao (codigo, pergunta) VALUES (%s, %s)"
        vals = (questao.getValues())
        mycursor.execute(sql, vals)
        self.connection.commit()
        return questao