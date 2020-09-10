from services.connection import Connection

class UniversidadeRepository:

    def __init__(self):
        self.connection = Connection('localhost', 'enade_pe', 'diogo', 'postgres').get()

    def insert(self, universidade):
        mycursor = self.connection.cursor()
        sql = "INSERT INTO universidade (dados) VALUES (%s, %s, %s, %s, %s)"
        vals = (universidade)
        mycursor.execute(sql, vals)
        self.connection.commit()