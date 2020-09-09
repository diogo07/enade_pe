
class MakeSQL:
    def __init__(self, data, ano):
        self.data = data
        self.ano = ano

    def getData(self):
        for index, row in self.data.iterrows():
            sql_universidade = "INSERT INTO universidade(codigo_ies, codigo_categoria, codigo_organizacao_academica, codigo_municipio) VALUES({}, {}, {}, {});".format(self.toInt(row['CO_IES']), self.toInt(row['CO_CATEGAD']), self.toInt(row['CO_ORGACAD']), self.toInt(row['CO_MUNIC_CURSO']))
            sql_curso = "INSERT INTO curso(turno, id_universidade, codigo, codigo_modalidade) VALUES('{}', {}, {}, {});".format(self.getTurno(row), self.toInt(row['CO_IES']), self.toInt(row['CO_CURSO']), self.toInt(row['CO_MODALIDADE']))
            sql_aluno = "INSERT INTO aluno(idade, sexo, ano_conc_ens_medio, ano_inic_grad) VALUES({}, '{}', {}, {});".format(self.toInt(row['NU_IDADE']), row['TP_SEXO'], self.getAnoConclusaoEnsinoMedio(row), self.toInt(row['ANO_IN_GRAD']))
            sql_enade = "INSERT INTO enade(ano, id_aluno, id_curso) VALUES({}, {}, {});".format(self.toInt(row['NU_ANO']), 0, 0)

            print(sql_universidade)
            print(sql_curso)
            print(sql_aluno)
            print(sql_enade)

            # QUESTOES DE PERCEPÇAO DA PROVA
            for i in range(1, 10):
                sql_resposta_percepcao_prova = "INSERT INTO resposta_percepcao_prova(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('CO_RS_I{}'.format(i), 0, row['CO_RS_I{}'.format(i)])
                print(sql_resposta_percepcao_prova)

            # QUESTÕES SOBRE O ESTUDANTE
            for i in range(1, 69):
                if i < 10:
                    sql_resposta_sobre_estudante = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I0{}'.format(i), 0, row['QE_I0{}'.format(i)])
                else:
                    sql_resposta_sobre_estudante = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I{}'.format(i), 0, row['QE_I{}'.format(i)])

                print(sql_resposta_sobre_estudante)


    def toInt(self, value):
        try:
            valueInt = int(value)
            return valueInt
        except:
            return 0

    def getTurno(self, row):
        if self.ano in [2014, 2015, 2016]:
            if row[14] == 1:
                return 'Matutino'
            elif row[15] == 1:
                return 'Vespertino'
            elif row[16] == 1:
                return 'Noturno'
            else:
                return 'Não Informado'
        else:
            if row['CO_TURNO_GRADUACAO'] == 1:
                return 'Matutino'
            elif row['CO_TURNO_GRADUACAO'] == 2:
                return 'Vespertino'
            elif row['CO_TURNO_GRADUACAO'] == 3:
                return 'Integral'
            elif row['CO_TURNO_GRADUACAO'] == 4:
                return 'Noturno'
            else:
                return 'Não Informado'

    def getAnoConclusaoEnsinoMedio(self, row):
        if self.ano in [2014, 2015, 2016]:
            return int(row['ANO_FIM_2G'])
        else:
            return int(row['ANO_FIM_EM'])

