class character:
    health = 100
    def __init__(self, Nname):
        self.name = Nname

    def __str__(self):
        return f"{self.name} has {self.health}HP "
    
    def __eq__(self, other):
        return isinstance(other, character) and self.name == other.name

    def __add__(self, other):
        return ([self, other])

    def attack(self, other):
        print(f"{self.name} is attacking {other.name} for 10 damage")

class hero(character):
    def attack(self, other):
        print(f"{self.name} is attacking {other.name} for 20 damage")

class witch():
    def __init__(self, Nname):
        self.name = Nname

bandit = character("Bandit")
aria = hero("Aria")

instn = bandit + aria
print(instn[1])

