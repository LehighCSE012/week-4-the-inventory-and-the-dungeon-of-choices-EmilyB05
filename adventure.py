"""Emily Byrnes - the inventory and the dungeon of choices- week 4 coding assignment"""
import random

inventory = []

def display_player_status(player_health):
    """displays the health of the player"""
    print(f"Your current health: {player_health}")

def handle_path_choice(player_health):
    """This function determines the path direction"""
    path = random.choice(["left", "right"])
    if path == "left":
        print("You encounter a friendly gnome who heals you for 10 health points.")
        player_health += 10
        if player_health > 100:
            player_health = 100
    if path == "right":
        print("You fall into a pit and lose 15 health points.")
        player_health -= 15
        if player_health < 0:
            player_health = 0
            print("You are barely alive!")
    return player_health

def player_attack(monster_health):
    """this function attacks the monster"""
    print("You strike the monster for 15 damage!")
    monster_health -= 15
    return monster_health

def monster_attack(player_health):
    """this function attacks the player"""
    critical_hit = random.choice([True, False])
    if critical_hit is True:
        player_health -= 20
        print("The monster lands a critical hit for 20 damage!")
    if critical_hit is False:
        player_health -= 10
        print("The monster hits you for 10 damage!")
    return player_health

def combat_encounter(player_health, monster_health, has_treasure):
    """this function is the combat sequence"""
    while player_health or monster_health > 0:
        monster_health = player_attack(monster_health)
        if monster_health <= 0:
            print("You defeated the monster!")
            break
        display_player_status(player_health)
        player_health = monster_attack(player_health)
        if player_health <= 0:
            print("Game Over!")
            break
    return has_treasure

def check_for_treasure(has_treasure):
    """This function determines if the player finds the treasure"""
    if has_treasure is True:
        print("You found the hidden treasure! You win!")
    if has_treasure is False:
        print("The monster did not have the treasure. You continue your journey.")

def aquire_item(inventory, item):
    inventory.append(item)
    print(f"You aquired a {item}!")
    return inventory

def display_inventory(inventory):
    if not inventory:
        print("Your inventory is empty.")  
    else:
        print("Your inventory:")
        print(*inventory, sep='\n')

def enter_dungeon(player_health, inventory, dungeon_rooms):
   for room in dungeon_rooms:
       print(f"You enter {room[0]}")
       print(f"You found a {room[1]}")
       aquire_item(inventory, room[1])
       if room[2] == "none":
           print("There doesn't seem to be a challenge in this room. You move on.")

       if room[2] == "puzzle":
        print("You encounter a puzzle!")
        solve_or_skip = input("Will you solve or skip the puzzle?")
        if solve_or_skip == "solve":
            solve_rate = random.choice([True, False])
            if solve_rate is True:
                print(room[3][0])
            else:
                print(room[3][1])
                print(f"You lost {room[3][2]} HP.")
                player_health += room[3][2]
        if solve_or_skip == "skip":
            print(room[3][1])
        
        if room[2] == "trap":
            print("You see a potential trap!")
            disarm_or_bypass = input("Will you disarm or bypass the trap?")
            if disarm_or_bypass == "disarm":
                disarm_rate = random.choice([True, False])
                if disarm_rate is True:
                    print(room[3][0])
                else:
                    print(room[3][1])
                    print(f"You lost {room[3][2]} HP.")
                    player_health += room[3][2]
            if disarm_or_bypass == "bypass":
                print(room[3][1])

        display_inventory(inventory)


        
    


def main():
    """This function manages the whole code"""
    player_health = 100
    monster_health = 75
    has_treasure = False
    has_treasure = random.choice([True, False])
    player_health = handle_path_choice(player_health)
    treasure_obtained_in_combat = combat_encounter(player_health, monster_health, has_treasure)
    check_for_treasure(treasure_obtained_in_combat)
    
    dungeon_rooms = [("A mysterious library", "book", "puzzle", ("You solved the puzzle!", "The puzzle remains unsolved.", -5)),
    ("a long hallway", "sword", "none", None), 
    ("a throne room", "crown", "trap", ("You escaped the trap!", "you were caught in the trap", -20))
    ]
    
    if player_health > 0:
        enter_dungeon(player_health, inventory, dungeon_rooms)

if __name__ == "__main__":
    main()
