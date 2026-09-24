class Circulo:
    raio:float

    def __init__(self, raio:float):
        self.raio = 10 if raio < 10 else raio 