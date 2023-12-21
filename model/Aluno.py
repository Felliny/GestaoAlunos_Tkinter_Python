from datetime import datetime


class Aluno:
    id = 0
    ra = 0
    nome = ""
    nascimento = ""

    def __init__(self, id, ra, nome, nascimento):
        self.id = id
        self.ra = ra
        self.nome = nome
        self.nascimento = self.set_nascimento(nascimento)

    def set_nascimento(self, nascimento):
        data_formatada = datetime.strptime(nascimento, "%d/%m/%Y")  # Transfoma uma string em data
        nascimento = data_formatada.strftime("%d/%m/%Y")  # Transforma uma data em string
        return nascimento
