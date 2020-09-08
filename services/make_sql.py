
class MakeSQL:
    def __init__(self, data, ano):
        self.data = data
        self.ano = ano

    def getData(self):
        for index, row in self.data.iterrows():
            sql_universidade = "INSERT INTO universidade(codigo_ies, codigo_categoria, codigo_organizacao_academica, codigo_municipio) VALUES({}, {}, {}, {});".format(self.toInt(row['CO_IES']), self.toInt(row['CO_CATEGAD']), self.toInt(row['CO_ORGACAD']), self.toInt(row['CO_MUNIC_CURSO']))
            sql_curso = "INSERT INTO curso(turno, id_universidade, codigo, codigo_modalidade) VALUES('{}', {}, {}, {});".format(self.getTurno(row), self.toInt(row['CO_IES']), self.toInt(row['CO_CURSO']), self.toInt(row['CO_MODALIDADE']))
            sql_aluno = "INSERT INTO aluno(idade, sexo, ano_conc_ens_medio, ano_inic_grad) VALUES({}, '{}', {}, {});".format(self.toInt(row['NU_IDADE']), row['TP_SEXO'], self.toInt(row['ANO_FIM_2G']), self.toInt(row['ANO_IN_GRAD']))
            sql_enade = "INSERT INTO enade(ano, id_aluno, id_curso) VALUES({}, {}, {});".format(self.toInt(row['NU_ANO']), 0, 0)
            sql_resposta_percepcao_prova_1 = "INSERT INTO resposta_percepcao_prova(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('CO_RS_I1', 0, row['CO_RS_I1'])
            sql_resposta_percepcao_prova_2 = "INSERT INTO resposta_percepcao_prova(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('CO_RS_I2', 0, row['CO_RS_I2'])
            sql_resposta_percepcao_prova_3 = "INSERT INTO resposta_percepcao_prova(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('CO_RS_I3', 0, row['CO_RS_I3'])
            sql_resposta_percepcao_prova_4 = "INSERT INTO resposta_percepcao_prova(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('CO_RS_I4', 0, row['CO_RS_I4'])
            sql_resposta_percepcao_prova_5 = "INSERT INTO resposta_percepcao_prova(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('CO_RS_I5', 0, row['CO_RS_I5'])
            sql_resposta_percepcao_prova_6 = "INSERT INTO resposta_percepcao_prova(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('CO_RS_I6', 0, row['CO_RS_I6'])
            sql_resposta_percepcao_prova_7 = "INSERT INTO resposta_percepcao_prova(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('CO_RS_I7', 0, row['CO_RS_I7'])
            sql_resposta_percepcao_prova_8 = "INSERT INTO resposta_percepcao_prova(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('CO_RS_I8', 0, row['CO_RS_I8'])
            sql_resposta_percepcao_prova_9 = "INSERT INTO resposta_percepcao_prova(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('CO_RS_I9', 0, row['CO_RS_I9'])
            sql_resposta_sobre_estudante_1 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I01', 0, row['QE_I01'])
            sql_resposta_sobre_estudante_2 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I02', 0, row['QE_I02'])
            sql_resposta_sobre_estudante_3 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I03', 0, row['QE_I03'])
            sql_resposta_sobre_estudante_4 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I04', 0, row['QE_I04'])
            sql_resposta_sobre_estudante_5 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I05', 0, row['QE_I05'])
            sql_resposta_sobre_estudante_6 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I06', 0, row['QE_I06'])
            sql_resposta_sobre_estudante_7 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I07', 0, row['QE_I07'])
            sql_resposta_sobre_estudante_8 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I08', 0, row['QE_I08'])
            sql_resposta_sobre_estudante_9 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I09', 0, row['QE_I09'])
            sql_resposta_sobre_estudante_10 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I10', 0, row['QE_I10'])
            sql_resposta_sobre_estudante_11 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I11', 0, row['QE_I11'])
            sql_resposta_sobre_estudante_12 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I12', 0, row['QE_I12'])
            sql_resposta_sobre_estudante_13 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I13', 0, row['QE_I13'])
            sql_resposta_sobre_estudante_14 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I14', 0, row['QE_I14'])
            sql_resposta_sobre_estudante_15 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I15', 0, row['QE_I15'])
            sql_resposta_sobre_estudante_16 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I16', 0, row['QE_I16'])
            sql_resposta_sobre_estudante_17 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I17', 0, row['QE_I17'])
            sql_resposta_sobre_estudante_18 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I18', 0, row['QE_I18'])
            sql_resposta_sobre_estudante_19 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I19', 0, row['QE_I19'])
            sql_resposta_sobre_estudante_20 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I20', 0, row['QE_I20'])
            sql_resposta_sobre_estudante_21 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I21', 0, row['QE_I21'])
            sql_resposta_sobre_estudante_22 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I22', 0, row['QE_I22'])
            sql_resposta_sobre_estudante_23 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I23', 0, row['QE_I23'])
            sql_resposta_sobre_estudante_24 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I24', 0, row['QE_I24'])
            sql_resposta_sobre_estudante_25 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I25', 0, row['QE_I25'])
            sql_resposta_sobre_estudante_26 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I26', 0, row['QE_I26'])
            print(sql_universidade)


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
            return int(row['ANO_FIM_2G'])

