
class Enade:

    def __init__(self, ano, idAluno, isCurso):
        self.id = None
        self.ano = ano
        self.idAluno = idAluno
        self.isCurso = isCurso

    def getValues(self):
        return (
            self.ano,
            self.idAluno,
            self.isCurso
        )