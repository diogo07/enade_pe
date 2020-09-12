
class Aluno:

    def __init__(self, idade, sexo, anoConclusaoEnsinoMedio, anoInicioGraduacao):
        self.id = None
        self.idade = idade
        self.sexo = sexo
        self.anoConclusaoEnsinoMedio = anoConclusaoEnsinoMedio
        self.anoInicioGraduacao = anoInicioGraduacao


    def getValues(self):
        return (
            self.idade,
            self.sexo,
            self.anoConclusaoEnsinoMedio,
            self.anoInicioGraduacao
        )