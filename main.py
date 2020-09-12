from _datetime import datetime

from models.aluno import Aluno
from models.curso import Curso
from models.enade import Enade
from models.resposta import Resposta
from models.universidade import Universidade
from repository.aluno_repository import AlunoRepository
from repository.curso_repository import CursoRepository
from repository.enade_repository import EnadeRepository
from repository.resposta_repository import RespostaRepository
from repository.universidade_repository import UniversidadeRepository
from services.load_txt import LoadTxt
from services.utils import *

import base
from services.connection import Connection
from constants.local import getCredentialsDatabase

if __name__ == '__main__':

    connection = Connection(getCredentialsDatabase()[0], getCredentialsDatabase()[1], getCredentialsDatabase()[2], getCredentialsDatabase()[3]).get()
    universidadeRepository = UniversidadeRepository(connection)
    cursoRepository = CursoRepository(connection)
    alunoRepository = AlunoRepository(connection)
    enadeRepository = EnadeRepository(connection)
    respostaRepository = RespostaRepository(connection)

    tempo_inicial = datetime.now()
    for ano in range(2014,2015):

        print('INICIANDO PROCESSAMENTO DOS DADOS DE {} ...'.format(ano))
        print('ABRINDO ARQUIVO ...')
        txt = LoadTxt('{}/enade_pe/data/MICRODADOS_ENADE_{}.txt'.format(base.path, ano), ano)
        data = txt.load()
        print(data)

        for index, row in data.iterrows():
            universidade = universidadeRepository.findOrInsertIfNotExist(Universidade(toInt(row['CO_IES']), toInt(row['CO_CATEGAD']), toInt(row['CO_ORGACAD']), toInt(row['CO_MUNIC_CURSO']), 'PE'))
            curso = cursoRepository.findOrInsertIfNotExist(Curso(getTurno(row), toInt(row['CO_IES']), toInt(row['CO_CURSO']), toInt(row['CO_MODALIDADE'])))
            aluno = alunoRepository.insert(Aluno(toInt(row['NU_IDADE']), row['TP_SEXO'], getAnoConclusaoEnsinoMedio(row), toInt(row['ANO_IN_GRAD'])))

            enade = enadeRepository.insert(Enade(toInt(row['NU_ANO']), aluno.id, curso.id))

            # QUESTOES DE PERCEPÇAO DA PROVA
            sql_respostas = "INSERT INTO resposta (codigo_questao, id_enade, opcao) VALUES (%s, %s, %s)"
            dados = []
            for i in range(1, 10):
                dados.append(('CO_RS_I{}'.format(i), enade.id, row['CO_RS_I{}'.format(i)]))

            # QUESTÕES SOBRE O ESTUDANTE
            for i in range(1, 69):
                if i < 10:
                    dados.append(('QE_I0{}'.format(i), enade.id, row['QE_I0{}'.format(i)]))
                else:
                    dados.append(('QE_I{}'.format(i), enade.id, row['QE_I{}'.format(i)]))
                    # list_respostas = list_respostas + "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I{}'.format(i), 0, row['QE_I{}'.format(i)])
                    # respostaRepository.insert(Resposta('QE_I{}'.format(i), enade.id, row['QE_I{}'.format(i)]))

            respostaRepository.insertMultipleRows(sql_respostas, dados)
    tempo_final = datetime.now()
    tempo_gasto = tempo_final - tempo_inicial
    print('TAREFA CONCLUÍDA COM SUCESSO EM {}'.format(tempo_gasto))