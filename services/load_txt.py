
class LoadTxt:
    def __init__(self, path):
        self.path = path
        self.header = None


    def load(self):
        file = open(self.path, "r")
        content = file.read()
        lines = content.split('-')
        self.header = lines[0]
        for line in lines:
            itens = line.split(';')
            # if itens[8] == '26':
            print(itens)