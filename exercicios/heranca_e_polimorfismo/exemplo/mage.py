from character import Character

class Mage(Character):

    attack_type:str

    def __init__(self, name):
        super().__init__(name, life = 100)
    
    def _toggle_attack_type(self, attack_type:str):
        if attack_type == None:
            self.attack_type = attack_type

    def attack(self, enemy: Character):
        if self.life < 50:
            self._toggle_attack_type('lightning')
            enemy.life-=35
        else:
            enemy.life-=30

