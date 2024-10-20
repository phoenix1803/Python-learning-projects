#a game using random module it runs by itself 
#and is a luck based game damage,loot generation etc is done using random

import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.treasure = 0

    def attack(self):
        return random.randint(10, 20)

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

class Monster:
    def __init__(self):
        self.health = random.randint(30, 60)

    def attack(self):
        return random.randint(5, 15)

def encounter_monster(player):
    monster = Monster()
    print("A wild monster appears!")
    
    while monster.health > 0 and player.health > 0:
        # Player's turn
        damage = player.attack()
        monster.health -= damage
        print(f"You attack the monster for {damage} damage.")
        print(f"Monster's health: {monster.health}")

        # Check if monster = defeated
        if monster.health <= 0:
            print("You defeated the monster!")
            treasure_found = random.randint(10, 50)
            player.treasure += treasure_found
            print(f"You found {treasure_found} treasure!")
            break

        # Monster's turn
        damage = monster.attack()
        player.take_damage(damage)
        print(f"The monster attacks you for {damage} damage.")
        print(f"Your health: {player.health}")

        # Check if player = defeated
        if player.health <= 0:
            print("You have been defeated. Game over!")
            return False

    return True

def explore_dungeon(player):
    while player.health > 0:
        print("\nYou explore the dungeon...")
        time.sleep(1)

        # Random encounter
        encounter = random.choice(["monster", "treasure", "nothing"])
        if encounter == "monster":
            if not encounter_monster(player):
                break
        elif encounter == "treasure":
            treasure_found = random.randint(5, 30)
            player.treasure += treasure_found
            print(f"You found {treasure_found} treasure!")
        else:
            print("You found nothing but dust...")

        # Check player's health
        if player.health <= 0:
            print("You have fallen in the dungeon. Game over!")
            break

def main():
    print("Welcome to the Dungeon Exploration Game!")
    name = input("Enter your character's name: ")
    player = Player(name)

    explore_dungeon(player)

    print(f"\nGame Over! You collected {player.treasure} treasure.")

if __name__ == "__main__":
    main()
