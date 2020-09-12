from services.connection import Connection

class UniversidadeRepository:

    def __init__(self, connection):
        self.connection = connection

    def insert(self, universidade):
        mycursor = self.connection.cursor()
        sql = "INSERT INTO universidade (codigo_ies, codigo_categoria, codigo_organizacao_academica, municipio, uf) VALUES (%s, %s, %s, %s, %s)  RETURNING id"
        vals = (universidade.getValues())
        mycursor.execute(sql, vals)
        self.connection.commit()

    def findOrInsertIfNotExist(self, universidade):
        findUniversidade = self.findByCodigo(universidade.codigoIES)
        if findUniversidade is None:
            universidade = self.insert(universidade)
            return universidade
        else:
            universidade.id = findUniversidade[0]
            return universidade


    def findByCodigo(self, codigoIES):
        mycursor = self.connection.cursor()
        sql = "SELECT * FROM universidade WHERE codigo_ies = {}".format(codigoIES)
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        if rows.__len__() > 0:
            return rows[0]
        else:
            return None

