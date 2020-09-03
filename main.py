from services.load_txt import LoadTxt
import base


if __name__ == '__main__':
    txt = LoadTxt('{}/enade_pe/data/MICRODADOS_ENADE_2010.txt'.format(base.path))
    txt.load()