from builtins import print

import pandas as pd
import os
from _datetime import datetime
from constants.columns import getColumnsData


class LoadTxt:
    def __init__(self, path, ano):
        self.path = path
        self.ano = ano
        self.header = None

    def load(self):
        if os.path.exists(self.path):
            tempo_inicial = datetime.now()
            print('LENDO DADOS ...')
            data = pd.read_csv(self.path, sep=";")

            print('SEPARANDO INFORMAÇÕES IMPORTANTES ...')

            # SELECIONANDO COLUNAS QUE SERÃO UTILIZADOS
            filter_columns = data.loc[:, getColumnsData(self.ano)]

            # CÓDIGO 26 SE REFERE AO ESTADO DE PERNAMBUCO
            filter_rows = filter_columns.query('CO_UF_CURSO == 26')

            tempo_final = datetime.now()
            tempo_gasto = tempo_final - tempo_inicial
            print('TAREFA CONCLUÍDA COM SUCESSO EM {}'.format(tempo_gasto))
            return filter_rows
        else:
            print('Erro: arquivo não existe!')


