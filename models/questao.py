
class Questao:

    def __init__(self, codigo, pergunta):
        self.id = None
        self.codigo = codigo
        self.pergunta = pergunta

    def getValues(self):
        return (
            self.codigo,
            self.pergunta
        )