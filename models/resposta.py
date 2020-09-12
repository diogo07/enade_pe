
class Resposta:

    def __init__(self, codigoQuestao, idEnade, opcao):
        self.id = None
        self.codigoQuestao = codigoQuestao
        self.idEnade = idEnade
        self.opcao = opcao

    def getValues(self):
        return (
            self.codigoQuestao,
            self.idEnade,
            self.opcao
        )