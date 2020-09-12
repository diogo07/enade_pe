def getTurno(row):
    if row['NU_ANO'] in [2014, 2015, 2016]:
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


def toInt(value):
    try:
        valueInt = int(value)
        return valueInt
    except:
        return 0


def getAnoConclusaoEnsinoMedio(row):
    if row['NU_ANO'] in [2014, 2015, 2016]:
        return int(row['ANO_FIM_2G'])
    else:
        return int(row['ANO_FIM_EM'])
