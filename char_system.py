class Entity:
    some_var = "default"   

    def __init__(self, health = 99, mana = 99):
        self.health = health
        self.mana   = mana

    def attack(self):
        print("attack!")
    def defend(self):
        print("defend!")
class Enemy(Entity):

    def __init__(self, health=99, mana=99):
        super().__init__(health=health, mana=mana)

class Character(Entity):

    def __init__(self, health, mana,stamina):
        super().__init__(health,mana)
        self.stamina = stamina
        
    def set_name(self):
        self.name = input("What is your name?\n")
        # print("Welcome, " + name + "!")

    def check_attribute(self):
        print("Health" + str(self.health))
        print("Name" + str(self.name))
        print("Stamina" + str(self.stamina))
        print("Mana" + str(self.mana))

    def character_Stats(self, char_class):
        char_class = char_class.lower()
        if char_class == "paladin":
            self.health += 20
            self.mana   += 30
        elif char_class == "warlock":
            self.health -= 20
            self.mana   += 30    
        elif char_class == "rogue":
            self.mana   -= 40

def main():
    enemy_character = Enemy()
    print(enemy_character.health)
    # main_character = Character(100,100,100)
    # main_character.set_name()
    # main_character.check_attribute()
    # main_character.attack()
    # char_class = input("""Select Your Class\n1.Paladin\n2.Warlock\n3.Rogue""")
    # main_character.character_Stats("warlock")
    # main_character.check_attribute()
    # print(main_character.some_var)

if __name__ == "__main__":
    main()
