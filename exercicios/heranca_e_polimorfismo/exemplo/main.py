from warrior import Warrior
from mage import Mage

if __name__ == '__main__':
    wizard = Mage("Ciri")
    warrior = Warrior("Geralt")
    enemy = Warrior("Irilith")

    wizard.attack(enemy)
    warrior.attack(enemy)
    
    print(enemy.life)

    for i in range(0, 8):
        enemy.attack(warrior)

    warrior.attack(enemy) # warrior deve dar 50 de dano
    print(enemy.life)