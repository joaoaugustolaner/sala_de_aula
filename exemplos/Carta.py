class Carta:

    remente:str
    destinatario:str
    conteudo:str

    def __init__(self, 
                 rementente:str, 
                 destinatario:str, 
                 conteudo:str):
        self.conteudo = conteudo
        self.destinatario = destinatario
        self.remente = rementente

#Instancia
carta = Carta('João', 'Pyetra', 'Te amo ❤️')

