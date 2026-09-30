class Character:
    name:str
    life:int
    level:int = 1

    def __init__(self, name:str, life:int):
        self.name = name
        self.life = life