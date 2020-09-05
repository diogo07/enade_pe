from builtins import print

import pandas as pd
import os
from _datetime import datetime

class LoadTxt:
    def __init__(self, path):
        self.path = path
        self.header = None


    def load(self):
        if os.path.exists(self.path):
            tempo_inicial = datetime.now()
            print('LENDO DADOS ...')
            data = pd.read_csv(self.path, sep=";")
            list = data.values.tolist()
            dados_pernambuco = []
            print('SEPARANDO INFORMAÇÕES IMPORTANTES ...')
            for row in list:
                # CÓDIGO 26 SE REFERE AO ESTADO DE PERNAMBUCO
                if row[8] == 26:
                    dados_pernambuco.append(row)
            tempo_final = datetime.now()
            tempo_gasto = tempo_final - tempo_inicial
            print('TAREFA CONCLUÍDA COM SUCESSO EM {}'.format(tempo_gasto))
            return dados_pernambuco
        else:
            print('Erro: arquivo não existe!')
