import random

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.level = 1
        self.experience = 0

    def is_alive(self):
        return self.health > 0

    def level_up(self):
        self.level += 1
        self.health += 10
        self.attack += 2
        self.defense += 2
        print(f"\n{self.name}, you've leveled up! You are now level {self.level}.")
        print(f"Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}")

    def gain_experience(self, amount):
        self.experience += amount
        print(f"\n{self.name}, you gained {amount} experience points.")
        if self.experience >= self.level * 10:
            self.level_up()

class Demon:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.health > 0

def battle(player, demon):
    print(f"\nA battle begins between {player.name} and {demon.name}!")
    while player.is_alive() and demon.is_alive():
        print(f"\n{player.name}'s Health: {player.health}, {demon.name}'s Health: {demon.health}")
        action = input("Do you want to attack, defend, or use a special move? (attack/defend/special): ").lower()

        if action == "attack":
            damage = max(0, player.attack - demon.defense)
            demon.health -= damage
            print(f"\n{player.name} attacks and deals {damage} damage to {demon.name}.")

        elif action == "defend":
            print(f"\n{player.name} prepares to defend.")
            player.defense += 2
            continue

        elif action == "special":
            if player.level >= 3:
                special_damage = player.attack * 2
                demon.health -= special_damage
                print(f"\n{player.name} uses a special move and deals {special_damage} damage to {demon.name}.")
            else:
                print("\nYou need to be at least level 3 to use a special move.")
                continue

        else:
            print("Not a valid option. You lose your turn.")
            continue

        if demon.is_alive():
            demon_damage = max(0, demon.attack - player.defense)
            player.health -= demon_damage
            print(f"\n{demon.name} attacks and deals {demon_damage} damage to {player.name}.")

    if player.is_alive():
        print(f"\n{player.name} has defeated {demon.name}!")
        player.gain_experience(10)
    else:
        print(f"\n{player.name} has been defeated by {demon.name}. Game Over.")

def start_game():
    print("Welcome to Demon Slayer: The Enhanced Adventure!")
    name = input("What is your name, young demon slayer? ")
    player = Character(name, health=50, attack=10, defense=5)
    print(f"Welcome, {player.name}. You are a newly recruited member of the Demon Slayer Corps.")
    print("Your mission is to defeat the powerful demons that terrorize the land and protect the innocent.")
    print("Your choices and skills will determine your fate. Choose wisely.")
    first_choice(player)

def first_choice(player):
    print("\nYou start your journey in a small village at the edge of a dark forest.")
    print("The villagers have reported strange occurrences, and you suspect a demon may be nearby.")
    answer = input("Do you want to investigate the forest or stay in the village to gather more information? (forest/village): ").lower()

    if answer == "forest":
        forest_path(player)
    elif answer == "village":
        village_path(player)
    else:
        print("Not a valid option. Please choose again.")
        first_choice(player)

def forest_path(player):
    print(f"\n{player.name}, you bravely enter the dark forest, guided by your instincts.")
    print("The trees are tall and ominous, and the air feels heavy.")
    print("You hear a faint noise in the distance, like someone crying.")
    answer = input("Do you want to follow the sound or ignore it and continue deeper into the forest? (follow/ignore): ").lower()

    if answer == "follow":
        follow_sound(player)
    elif answer == "ignore":
        deeper_forest(player)
    else:
        print("Not a valid option. Please choose again.")
        forest_path(player)

def village_path(player):
    print(f"\n{player.name}, you decide to stay in the village to gather more information.")
    print("You meet an old woman who tells you about a haunted mansion nearby, believed to be the lair of a demon.")
    answer = input("Do you want to investigate the mansion or continue questioning the villagers? (mansion/question): ").lower()

    if answer == "mansion":
        mansion_path(player)
    elif answer == "question":
        question_villagers(player)
    else:
        print("Not a valid option. Please choose again.")
        village_path(player)

def follow_sound(player):
    print(f"\n{player.name}, you follow the sound and find a young girl crying by a tree.")
    print("As you approach, she reveals herself to be a demon in disguise!")
    demon = Demon(name="Demon Girl", health=30, attack=8, defense=3)
    battle(player, demon)
    if player.is_alive():
        print("You have defeated the demon and saved the village. You WIN!")

def deeper_forest(player):
    print(f"\n{player.name}, you ignore the sound and venture deeper into the forest.")
    print("Suddenly, you are ambushed by a powerful demon!")
    demon = Demon(name="Forest Demon", health=40, attack=10, defense=5)
    battle(player, demon)
    if player.is_alive():
        print("You have defeated the powerful demon and saved the forest. You WIN!")

def mansion_path(player):
    print(f"\n{player.name}, you arrive at the haunted mansion. The atmosphere is eerie, and you can feel the presence of a demon.")
    print("You explore the mansion and find a hidden door leading to a secret chamber.")
    answer = input("Do you want to enter the chamber or explore the rest of the mansion first? (chamber/explore): ").lower()

    if answer == "chamber":
        secret_chamber(player)
    elif answer == "explore":
        explore_mansion(player)
    else:
        print("Not a valid option. Please choose again.")
        mansion_path(player)

def question_villagers(player):
    print(f"\n{player.name}, you continue questioning the villagers and learn about a demon hunter who went missing.")
    print("You decide to search for clues about the demon hunter's whereabouts.")
    answer = input("Do you want to search the village or head towards the forest where the hunter was last seen? (village/forest): ").lower()

    if answer == "village":
        search_village(player)
    elif answer == "forest":
        hunter_forest(player)
    else:
        print("Not a valid option. Please choose again.")
        question_villagers(player)

def secret_chamber(player):
    print(f"\n{player.name}, you enter the secret chamber and find a powerful artifact that can help you defeat demons.")
    print("However, the artifact is cursed, and using it comes at a great cost.")
    answer = input("Do you want to take the artifact or leave it behind? (take/leave): ").lower()

    if answer == "take":
        print(f"\n{player.name}, you take the artifact and feel a surge of power. However, the curse begins to take hold.")
        player.attack += 5
        player.defense -= 3
        player.health -= 10
        demon = Demon(name="Mansion Demon", health=50, attack=12, defense=6)
        battle(player, demon)
        if player.is_alive():
            print("You defeated the demon but the curse slowly consumes you. You win, but at a great cost.")
    elif answer == "leave":
        print(f"\n{player.name}, you decide that the artifact is too dangerous and leave it behind.")
        demon = Demon(name="Mansion Demon", health=50, attack=12, defense=6)
        battle(player, demon)
        if player.is_alive():
            print("You defeated the demon and are hailed as a hero. You WIN!")
    else:
        print("Not a valid option. Please choose again.")
        secret_chamber(player)

def explore_mansion(player):
    print(f"\n{player.name}, you decide to explore the rest of the mansion first.")
    print("As you do, you trigger a trap set by the demon. You are captured and defeated. You lose.")

def search_village(player):
    print(f"\n{player.name}, you search the village and find clues leading to a hidden cave where the demon hunter was taken.")
    print("You rescue the hunter and together you defeat the demon. You WIN!")

def hunter_forest(player):
    print(f"\n{player.name}, you head towards the forest where the hunter was last seen.")
    print("You find the hunter's belongings, but the demon responsible for the hunter's disappearance finds you.")
    demon = Demon(name="Hunter's Demon", health=45, attack=11, defense=7)
    battle(player, demon)
    if player.is_alive():
        print("You fought bravely and defeated the demon. You WIN!")

# Start the game
start_game()
