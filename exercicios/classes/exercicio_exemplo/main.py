from aluno import Aluno
from prova import Prova

if __name__ == '__main__':
    aluno = Aluno("João", Prova("Lógica", 9.0))
    aluno.exibir_prova()