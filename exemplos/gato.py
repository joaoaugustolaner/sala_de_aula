class Gato:

    pelagem:str
    porte:str
    idade:int
    nome:str

    def __init__(self, 
                 pelagem:str, 
                 porte:str, 
                 idade:int, 
                 nome:str):
        self.pelagem = pelagem
        self.porte = porte
        self.nome = nome
        self.idade = idade if idade > 1 else 1
