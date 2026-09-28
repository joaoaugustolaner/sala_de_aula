from prova import Prova as p

class Aluno:

    nome:str
    prova:p

    def __init__(self, nome:str, prova:p):
        self.nome = nome
        self.prova = prova

    def exibir_prova(self):
        print(f"A prova é {self.prova.materia} e a nota é {self.prova.nota}")