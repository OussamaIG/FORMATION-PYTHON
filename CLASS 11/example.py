class Character:

    Level = 0

    def __init__(self, Nname, Nhealth):
        self.name = Nname
        self.health = Nhealth
        
    def attack(self, other):
        print(f"{self.name} -> attack {other.name} for 10 damage")
        other.take_damage(10)

    def take_damage(self, amount):
        self.health = max(self.health - amount, 0)
        print(f"{self.name} now has {self.health} HP")

class Hero(Character):

    charge = 0
    
    def __init__(self, Nname, Nhealth):
        super().__init__(Nname, Nhealth)

    def attack(self, other):
        super().attack(other)
        self.charge = self.charge + 10
        print(f"hero charge is at {self.charge}%")
        if(self.charge == 100):
            self.super_attack(other)

    def super_attack(self, other):
        print(f"{self.name} uses SUPER POWER on {other.name}")
        other.take_damage(other.health)
        self.Level = self.Level + 1

class Wizard(Character):
    def __init__(self, Nname, Nhealth, Nmana):
        super().__init__(Nname, Nhealth)
        self.mana = Nmana
    
    def cast_spell(self, other):
        if self.mana >= 10:
            self.mana -= 10
            print(f"{self.name} casts a spell on {other.name}!")
            other.take_damage(50)
        else :
            print(f"{self.name} is out of mana")



char = Character("Jacksper", 50)
goblin = Character("Fredo", 1000)
hero = Hero("Aria", 150)
wiz = Wizard("Harry", 200, 50)

while True :
    hero.attack(goblin)
    if goblin.health == 0:
        break
    goblin.attack(hero)
    
print(hero.Level)
wiz.cast_spell(hero)





