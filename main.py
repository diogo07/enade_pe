from services.load_txt import LoadTxt
import base


if __name__ == '__main__':
    print('INICIANDO PROCESSAMENTO DOS DADOS ...')
    print('ABRINDO ARQUIVO ...')
    txt = LoadTxt('{}/enade_pe/data/MICRODADOS_ENADE_2010.txt'.format(base.path))
    enade_pernambuco_2010 = txt.load()

