from emitir_contato import EmitirContato
from aluno import Aluno

if __name__ == '__main__':
    aluno = Aluno("João", 28, "blablabla@whiskas-sache.com")
    contato = EmitirContato(aluno)
    contato.escrever_arquivo()