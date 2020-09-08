from services.load_txt import LoadTxt
from services.make_sql import MakeSQL
import base


if __name__ == '__main__':
    print('INICIANDO PROCESSAMENTO DOS DADOS ...')
    print('ABRINDO ARQUIVO ...')
    txt = LoadTxt('{}/enade_pe/data/MICRODADOS_ENADE_2017.txt'.format(base.path), 2018)
    enade_pernambuco_2018 = txt.load()

    make_sql = MakeSQL(enade_pernambuco_2018)
    make_sql.getData()
    # txt = LoadTxt('{}/enade_pe/data/MICRODADOS_ENADE_2011.txt'.format(base.path))
    # enade_pernambuco_2011 = txt.load()

