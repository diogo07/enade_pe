
class AlunoRepository:

    def __init__(self, connection):
        self.connection = connection

    def insert(self, aluno):
        mycursor = self.connection.cursor()
        sql = "INSERT INTO aluno (idade, sexo, ano_conc_ens_medio, ano_inic_grad) VALUES (%s, %s, %s, %s)  RETURNING id"
        vals = (aluno.getValues())
        mycursor.execute(sql, vals)
        self.connection.commit()
        aluno.id = mycursor.fetchone()[0]
        return aluno

