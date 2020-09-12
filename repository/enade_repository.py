
class EnadeRepository:

    def __init__(self, connection):
        self.connection = connection

    def insert(self, enade):
        mycursor = self.connection.cursor()
        sql = "INSERT INTO enade (ano, id_aluno, id_curso) VALUES (%s, %s, %s) RETURNING id"
        vals = (enade.getValues())
        mycursor.execute(sql, vals)
        self.connection.commit()
        enade.id = mycursor.fetchone()[0]
        return enade