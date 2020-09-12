
class Curso:

    def __init__(self, turno, codigoUniversidade, codigo, codigoModalidade):
        self.id = None
        self.turno = turno
        self.codigoUniversidade = codigoUniversidade
        self.codigo = codigo
        self.codigoModalidade = codigoModalidade

    def getValues(self):
        return (
            self.turno,
            self.codigoUniversidade,
            self.codigo,
            self.codigoModalidade
        )

    def __str__(self):
        return ' id: {} \n turno: {} \n codigoUniversidade: {} \n codigo: {} \n codigoModalidade: {}'.format(self.id, self.turno, self.codigoUniversidade, self.codigo, self.codigoModalidade)