class Aluno:
    
    nome:str
    idade:int
    email:str

    def __init__(self, nome:str, idade:int, email:str):
        self.nome = nome
        self.idade = idade
        self.email = email
    
    def __str__(self):
        return f"\nMeu nome é: {self.nome}\nMinha idade é: {self.idade}\nE para entrar em contato comigo use: {self.email}"
