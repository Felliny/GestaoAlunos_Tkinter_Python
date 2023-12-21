from model.Aluno import Aluno


class GestaoAlunosController:
    indice = 0
    alunos = []

    nome = ""
    nascimento = ""

    def cadastrar(self, ra, nome, nascimento):
        aluno = Aluno(self.indice, ra, nome, nascimento)

        self.alunos.append(aluno)
        self.indice += 1

    def remover(self, ra):
        for aluno in self.alunos:
            if ra == aluno.ra:
                self.alunos.remove(aluno)
                self.limparDados()

    def pesquisar(self, ra):
        for aluno in self.alunos:
            if ra == aluno.ra:
                self.nome = aluno.nome
                self.nascimento = aluno.nascimento


    def limparDados(self):
        self.nome = ""
        self.nascimento = ""
