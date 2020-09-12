from models.curso import Curso
from repository.curso_repository import CursoRepository
from services.utils import *

class CursoResource:

    def __init__(self, data, ano, connection):
        self.data = data
        self.ano = ano
        self.connection = connection

    def readAndSave(self):

        cursoRepository = CursoRepository(self.connection)
        for index, row in self.data.iterrows():
            cursoRepository.findOrInsertIfNotExist(Curso(getTurno(row), toInt(row['CO_IES']), toInt(row['CO_CURSO']), toInt(row['CO_MODALIDADE'])))