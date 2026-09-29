class Animal:
    nome: str

    def __init__(self, nome:str):
        self.nome = nome
        
    def fazer_som(self):
        return "..."