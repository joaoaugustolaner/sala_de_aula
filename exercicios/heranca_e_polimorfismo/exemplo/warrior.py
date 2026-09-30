from character import Character

class Warrior(Character):

    rage: bool = False

    def __init__(self, name):
        super().__init__(name, life = 150)
    
    def _toggle_rage(self):
        if not self.rage:
            self.rage = True
        else:
            self.rage = False

    def attack(self, enemy: Character):
        if self.life < 30:
            self._toggle_rage()
            enemy.life -= 50
        else:
            enemy.life -= 20
    
