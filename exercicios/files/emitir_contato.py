from aluno import Aluno

class EmitirContato:
    aluno:Aluno

    def __init__(self, aluno: Aluno):
        self.aluno = aluno
    
    def escrever_arquivo(self):
        with open('exercicios/files/aluno.txt', 'w', encoding='utf-8') as f:
            f.write(self.aluno.__str__())
