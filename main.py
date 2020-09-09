from services.load_txt import LoadTxt
from services.make_sql import MakeSQL
import base


if __name__ == '__main__':

    for ano in range(2014,2019):

        print('INICIANDO PROCESSAMENTO DOS DADOS DE {} ...'.format(ano))
        print('ABRINDO ARQUIVO ...')
        txt = LoadTxt('{}/enade_pe/data/MICRODADOS_ENADE_{}.txt'.format(base.path, ano), ano)
        enade_pernambuco = txt.load()
        make_sql = MakeSQL(enade_pernambuco, ano)
        make_sql.getData()

