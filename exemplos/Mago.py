class Mago:

    pontos_de_vida: int
    pontos_de_magia: int
    capacidade:int = 50

    def __init__(self, 
                 pontos_de_vida:int, 
                 pontos_de_magia:int):
        self.pontos_de_vida = pontos_de_vida
        self.pontos_de_magia = pontos_de_magia


#Instancia
mago = Mago(30, 50) #ou
mago_vekna = Mago(pontos_de_magia=50, pontos_de_vida=30)

