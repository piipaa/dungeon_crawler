# important functions for this program
def isvalidnumber(text): # checks if input is a number
    try: 
        int(text)
        return int(text)
    except ValueError:
        print("Please only input numbers!!")
        return None

#template for character creation
class PlayerCharacter:
    all_characters = [] 
    def __init__(self, name, armor_class, max_health):
        self.name = name.title()
        self.armor_class = armor_class
        self.max_health = max_health
        self.initiative = 0
        PlayerCharacter.all_characters.append(self)
    
    def input_ac():
        armor_class = None
        while armor_class is None:
            armor_class = input("Enter your character's armor class:")
            armor_class = isvalidnumber(armor_class)
        return armor_class

    def input_hp():
        max_health = None
        while max_health is None:
            max_health = input("Enter your character's maximum health:")
            max_health = isvalidnumber(max_health) 
        return max_health


class EnemyCharacter:
    all_enemies = [] 
    def __init__(self, name, armor_class, max_health):
        self.name = name.title()
        self.armor_class = armor_class
        self.max_health = max_health
        self.initiative = 0
        EnemyCharacter.all_enemies.append(self)
    
    def input_ac():
        armor_class = None
        while armor_class is None:
            armor_class = input("Enter the foe's armor class:")
            armor_class = isvalidnumber(armor_class)
        return armor_class

    def input_hp():
        max_health = None
        while max_health is None:
            max_health = input("Enter the foe's maximum health:")
            max_health = isvalidnumber(max_health) 
        return max_health
