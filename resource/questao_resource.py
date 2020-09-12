from models.questao import Questao
from repository.questao_repository import QuestaoRepository
import base, pandas as pd

class QuestaoResource:

    def __init__(self, connection):
        self.connection = connection

    def readAndSave(self):
        questaoRepository = QuestaoRepository(self.connection)
        data = pd.read_csv('{}/enade_pe/about/questions.txt'.format(base.path), sep=";")
        for index, row in data.iterrows():
            questaoRepository.insert(Questao(row['CODIGO'], row['QUESTAO']))