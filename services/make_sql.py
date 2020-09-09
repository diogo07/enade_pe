
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


            sql_resposta_sobre_estudante_27 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I27', 0, row['QE_I27'])
            sql_resposta_sobre_estudante_28 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I28', 0, row['QE_I28'])
            sql_resposta_sobre_estudante_29 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I29', 0, row['QE_I29'])
            sql_resposta_sobre_estudante_30 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I30', 0, row['QE_I30'])
            sql_resposta_sobre_estudante_31 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I31', 0, row['QE_I31'])
            sql_resposta_sobre_estudante_32 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I32', 0, row['QE_I32'])
            sql_resposta_sobre_estudante_33 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I33', 0, row['QE_I33'])
            sql_resposta_sobre_estudante_34 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I34', 0, row['QE_I34'])
            sql_resposta_sobre_estudante_35 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I35', 0, row['QE_I35'])
            sql_resposta_sobre_estudante_36 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I36', 0, row['QE_I36'])
            sql_resposta_sobre_estudante_37 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I37', 0, row['QE_I37'])
            sql_resposta_sobre_estudante_38 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I38', 0, row['QE_I38'])
            sql_resposta_sobre_estudante_39 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I39', 0, row['QE_I39'])
            sql_resposta_sobre_estudante_40 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I40', 0, row['QE_I40'])
            sql_resposta_sobre_estudante_41 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I41', 0, row['QE_I41'])
            sql_resposta_sobre_estudante_42 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I42', 0, row['QE_I42'])
            sql_resposta_sobre_estudante_43 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I43', 0, row['QE_I43'])
            sql_resposta_sobre_estudante_44 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I44', 0, row['QE_I44'])
            sql_resposta_sobre_estudante_45 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I45', 0, row['QE_I45'])
            sql_resposta_sobre_estudante_46 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I46', 0, row['QE_I46'])
            sql_resposta_sobre_estudante_47 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I47', 0, row['QE_I47'])
            sql_resposta_sobre_estudante_48 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I48', 0, row['QE_I48'])
            sql_resposta_sobre_estudante_49 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I49', 0, row['QE_I49'])
            sql_resposta_sobre_estudante_50 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I50', 0, row['QE_I50'])
            sql_resposta_sobre_estudante_51 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I51', 0, row['QE_I51'])
            sql_resposta_sobre_estudante_52 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I52', 0, row['QE_I52'])
            sql_resposta_sobre_estudante_53 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I53', 0, row['QE_I53'])
            sql_resposta_sobre_estudante_54 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I54', 0, row['QE_I54'])
            sql_resposta_sobre_estudante_55 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I55', 0, row['QE_I55'])
            sql_resposta_sobre_estudante_56 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I56', 0, row['QE_I56'])
            sql_resposta_sobre_estudante_57 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I57', 0, row['QE_I57'])
            sql_resposta_sobre_estudante_58 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I58', 0, row['QE_I58'])
            sql_resposta_sobre_estudante_59 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I59', 0, row['QE_I59'])
            sql_resposta_sobre_estudante_60 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I60', 0, row['QE_I60'])
            sql_resposta_sobre_estudante_61 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I61', 0, row['QE_I61'])
            sql_resposta_sobre_estudante_62 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I62', 0, row['QE_I62'])
            sql_resposta_sobre_estudante_63 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I63', 0, row['QE_I63'])
            sql_resposta_sobre_estudante_64 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I64', 0, row['QE_I64'])
            sql_resposta_sobre_estudante_65 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I65', 0, row['QE_I65'])
            sql_resposta_sobre_estudante_66 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I66', 0, row['QE_I66'])
            sql_resposta_sobre_estudante_67 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I67', 0, row['QE_I67'])
            sql_resposta_sobre_estudante_68 = "INSERT INTO resposta_sobre_estudante(codigo_questao, id_enade, opcao) VALUES({}, {}, '{}');".format('QE_I68', 0, row['QE_I68'])


            print(sql_universidade)
            print(sql_curso)
            print(sql_aluno)
            print(sql_enade)
            print(sql_resposta_percepcao_prova_1)
            print(sql_resposta_percepcao_prova_2)
            print(sql_resposta_percepcao_prova_3)
            print(sql_resposta_percepcao_prova_4)
            print(sql_resposta_percepcao_prova_5)
            print(sql_resposta_percepcao_prova_6)
            print(sql_resposta_percepcao_prova_7)
            print(sql_resposta_percepcao_prova_8)
            print(sql_resposta_percepcao_prova_9)
            print(sql_resposta_sobre_estudante_1)
            print(sql_resposta_sobre_estudante_2)
            print(sql_resposta_sobre_estudante_3)
            print(sql_resposta_sobre_estudante_4)
            print(sql_resposta_sobre_estudante_5)
            print(sql_resposta_sobre_estudante_6)
            print(sql_resposta_sobre_estudante_7)
            print(sql_resposta_sobre_estudante_8)
            print(sql_resposta_sobre_estudante_9)
            print(sql_resposta_sobre_estudante_10)
            print(sql_resposta_sobre_estudante_11)
            print(sql_resposta_sobre_estudante_12)
            print(sql_resposta_sobre_estudante_13)
            print(sql_resposta_sobre_estudante_14)
            print(sql_resposta_sobre_estudante_15)
            print(sql_resposta_sobre_estudante_16)
            print(sql_resposta_sobre_estudante_17)
            print(sql_resposta_sobre_estudante_18)
            print(sql_resposta_sobre_estudante_19)
            print(sql_resposta_sobre_estudante_20)
            print(sql_resposta_sobre_estudante_21)
            print(sql_resposta_sobre_estudante_22)
            print(sql_resposta_sobre_estudante_23)
            print(sql_resposta_sobre_estudante_24)
            print(sql_resposta_sobre_estudante_25)
            print(sql_resposta_sobre_estudante_26)
            print(sql_resposta_sobre_estudante_27)
            print(sql_resposta_sobre_estudante_28)
            print(sql_resposta_sobre_estudante_29)
            print(sql_resposta_sobre_estudante_30)
            print(sql_resposta_sobre_estudante_31)
            print(sql_resposta_sobre_estudante_32)
            print(sql_resposta_sobre_estudante_33)
            print(sql_resposta_sobre_estudante_34)
            print(sql_resposta_sobre_estudante_35)
            print(sql_resposta_sobre_estudante_36)
            print(sql_resposta_sobre_estudante_37)
            print(sql_resposta_sobre_estudante_38)
            print(sql_resposta_sobre_estudante_39)
            print(sql_resposta_sobre_estudante_40)
            print(sql_resposta_sobre_estudante_41)
            print(sql_resposta_sobre_estudante_42)
            print(sql_resposta_sobre_estudante_43)
            print(sql_resposta_sobre_estudante_44)
            print(sql_resposta_sobre_estudante_45)
            print(sql_resposta_sobre_estudante_46)
            print(sql_resposta_sobre_estudante_47)
            print(sql_resposta_sobre_estudante_48)
            print(sql_resposta_sobre_estudante_49)
            print(sql_resposta_sobre_estudante_50)
            print(sql_resposta_sobre_estudante_51)
            print(sql_resposta_sobre_estudante_52)
            print(sql_resposta_sobre_estudante_53)
            print(sql_resposta_sobre_estudante_54)
            print(sql_resposta_sobre_estudante_55)
            print(sql_resposta_sobre_estudante_56)
            print(sql_resposta_sobre_estudante_57)
            print(sql_resposta_sobre_estudante_58)
            print(sql_resposta_sobre_estudante_59)
            print(sql_resposta_sobre_estudante_60)
            print(sql_resposta_sobre_estudante_61)
            print(sql_resposta_sobre_estudante_62)
            print(sql_resposta_sobre_estudante_63)
            print(sql_resposta_sobre_estudante_64)
            print(sql_resposta_sobre_estudante_65)
            print(sql_resposta_sobre_estudante_66)
            print(sql_resposta_sobre_estudante_67)
            print(sql_resposta_sobre_estudante_68)


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

