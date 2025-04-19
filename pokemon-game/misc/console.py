import os
from characters import *

def clear_screen():
    os.system('clear')

def draw_game_screen(pokemon, position_x, position_y, width, height):
    
    # screen = [
    #     "+------------------------------------------------------------------------------+",
    #     "|                                                                              |",
    #     "|                                                                              |",
    #     "|                                                                              |",
    #     ...
    #     "+------------------------------------------------------------------------------+",
       
    # ]
    screen = [" " * width for x in range(height)]
    
    for i in range(height) :
        if i == 0 or i == height - 1:
            screen[i] = "+" + (width - 2) * "-" + "+"
        else:
            screen[i] = "|" + (width - 2) * " " + "|"

 # Insert the Pokémon at the specified position
    lines = pokemon.split("\n")
    for i, line in enumerate(lines):
        y_pos = position_y + i
        if 0 < y_pos < height - 1:  # Stay within border
            screen_line = list(screen[y_pos])
            for j, char in enumerate(line):
                x_pos = position_x + j
                if 0 < x_pos < width - 1 and char != " ":  # Stay within border and only draw non-space characters
                    screen_line[x_pos] = char
            screen[y_pos] = "".join(screen_line)
 # find out why is there a mislaient in lines 21-31. the problem is with the  picture itself.   the top lines are always displased . need to add more pokemon . add lines that gve us the ability to code how pokemon moves.         

    clear_screen()
    for line in screen:
        print(line)

    #while X >= 80:
    #coordinates_top_line = 0, X
    #X += 1

def main():
    position_x, position_y = 10, 10
    width, height = 80, 24
    
    import characters

    POKEMON_ASCII = {
    "EEVEE": EEVEE,
    "PIKACHU": PIKACHU,
    "BULBASAUR": BULBASAUR,
    "CHARMANDER": CHARMANDER,
    "JIGGLYPUFF": JIGGLYPUFF,
    "MEOWTH": MEOWTH,
    "SNORLAX": SNORLAX,
    "SQUIRTLE": SQUIRTLE,
    "PSYDUCK": PSYDUCK,
}
    current_pokemon = CHARMANDER

    draw_game_screen(current_pokemon, position_x, position_y, width, height)

    print("\nControls:")
    print("- w: Move up")
    print("- s: Move down")
    print("- a: Move left")
    print("- d: Move right")
    print("- p: Switch Pokémon")
    print("- q: Quit the game")

    # Main game loop
    running = True
    while running:
        draw_game_screen(current_pokemon, position_x, position_y, width, height)  
        # Ask for input (simple but reliable approach)
        command = input("Enter command (w/a/s/d/p/q): ").lower()
        # do smth
        if command == "q":
            running = False
        elif command == 'w':
            position_y = max(1, position_y - 1)  # Up
        elif command == 's':
            position_y = min(height - 2, position_y + 1)  # Down
        elif command == 'a':
            position_x = max(1, position_x - 1)  # Left
        elif command == 'd':
            position_x = min(width - 2, position_x + 1)  # Right


    print('Thank you for playing!')
    
if __name__ == "__main__":
    main()

