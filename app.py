from common.character_property import PlayerCharacter, EnemyCharacter

## PLAYER CHARACTER CREATION
# initializes 
player_names = []
player_count = int(input('How many players?\nEnter: '))
for i in range(player_count):
    name = input('what is your name?\nEnter: ')
    name = name.title()
    player_names.append(name)
print('There are', player_count, 'players')

# Iterates through list to apply PlayerCharacter class template
for player in player_names:
    character = PlayerCharacter(
    input("Enter %s's character name:" % player),
    PlayerCharacter.input_ac(),
    PlayerCharacter.input_hp()
    )
    
    print("""--Player %s Info--
    Name: %s
    Armor Class: %s
    Health: %s""" % (player, character.name, character.armor_class, character.max_health))

## ENEMY CHARACTER CREATION
# initialize
enemy_names = []
enemy_count = int(input("How many enemies?\nEnter: "))
for i in range(enemy_count):
    name = input("what kind of mob is this?\nEnter: ")
    name = name.title()
    enemy_names.append(name)
print("There are", enemy_count, "enemies")

for enemy in enemy_names:
    character = EnemyCharacter(
    input("Enter %s's character name:" % enemy),
    EnemyCharacter.input_ac(),
    EnemyCharacter.input_hp()
    )
    
    print("""--Enemy %s Info--
    Name: %s
    Armor Class: %s
    Health: %s""" % (enemy, character.name, character.armor_class, character.max_health))

in_initiative = input("Begin Initiative? (y/n)")

while in_initiative == "y" or in_initiative == "Y":
    ## player initiative
    # assigns d20 value to initiative_roll variable
    print("Starting initiative... all players please roll!")
    for character in PlayerCharacter.all_characters:
        PlayerCharacter.roll_for_initiative()
    # sort the list of characters by their initiative attribute value
    player_initiative_list = sorted(PlayerCharacter.all_characters, key=lambda character:character.initiative)
    
    ## enemy initiative
    # assigns d20 value to initiative_roll variable
    print("Starting initiative... all enemies please roll!")
    for character in EnemyCharacter.all_enemies:
        EnemyCharacter.roll_for_initiative()

    # sort the list of characters by their initiative attribute value
    enemy_initiative_list = sorted(EnemyCharacter.all_enemies, key=lambda character:character.initiative)

    total_initiative_list = player_initiative_list + enemy_initiative_list
    total_sorted_initiative_list = sorted(total_initiative_list, key=lambda character:character.initiative)

    print("""The initiative order is...
    ---""")
    for character in total_sorted_initiative_list:
        print("%s with a roll of %s" % (character.name, character.initiative))

    finished = input("Done? (y/n)")
    if finished == "y" or finished == "Y":
        for character in PlayerCharacter.all_characters:
            character.initiative = 0
            print("%s initiative is now %d." % (character.name, character.initiative))
        for character in EnemyCharacter.all_enemies:
            character.initiative = 0
            print("%s initiative is now %d." % (character.name, character.initiative))
        print("""Cleared initiative rolls. 
        Thanks for playing! 
        Exiting program...""")
        #in_initiative = False
        break
