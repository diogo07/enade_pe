
class CursoRepository:

    def __init__(self, connection):
        self.connection = connection

    def insert(self, curso):
        mycursor = self.connection.cursor()
        sql = "INSERT INTO curso (turno, codigo_universidade, codigo, codigo_modalidade) VALUES (%s, %s, %s, %s) RETURNING id"
        vals = (curso.getValues())
        mycursor.execute(sql, vals)
        self.connection.commit()
        curso.id = mycursor.fetchone()[0]
        return curso

    def findOrInsertIfNotExist(self, curso):
        findCurso = self.findByCodigos(curso.codigo, curso.codigoUniversidade)
        if findCurso is None:
            return self.insert(curso)
        else:
            curso.id = findCurso[0]
            return curso

    def findByCodigos(self, codigoCurso, codigoUniversidade):
        mycursor = self.connection.cursor()
        sql = "SELECT * FROM curso WHERE codigo = {} AND codigo_universidade = {}".format(codigoCurso, codigoUniversidade)
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        if rows.__len__() > 0:
            return rows[0]
        else:
            return None

