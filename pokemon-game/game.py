import os
from characters import *

# Function to clear the screen for better gameplay experience
def clear_screen():
    # Clears the screen, works on both Windows ('cls') and Linux/Mac ('clear')
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to draw the game screen and display Pokémon
def draw_game_screen(pokemon, position_x, position_y, width, height):
    # Initialize an empty screen with border characters
    screen = []

    # Build border
    for i in range(height):
        if i == 0 or i == height - 1:
            # Top and bottom borders
            screen.append("+" + (width - 2) * "-" + "+")
        else:
            # Left and right borders with space in between
            screen.append("|" + (width - 2) * " " + "|")

    # Split Pokémon ASCII art into lines and insert it into the game screen
    lines = pokemon.strip("\n").split("\n")
    for i, line in enumerate(lines):
        y_pos = position_y + i
        if 0 < y_pos < height - 1:
            # Modify the screen to place Pokémon
            screen_line = list(screen[y_pos])
            for j, char in enumerate(line):
                x_pos = position_x + j
                if 0 < x_pos < width - 1 and char != " ":
                    # Place the character if it’s not a space
                    screen_line[x_pos] = char
            screen[y_pos] = "".join(screen_line)

    # Clear the terminal screen before drawing
    clear_screen()

    # Print the final screen
    for line in screen:
        print(line)

# Function to print controls for the player
def print_controls():
    print("\nControls:")
    print("- w: Move up")
    print("- s: Move down")
    print("- a: Move left")
    print("- d: Move right")
    print("- p: Switch Pokémon")
    print("- q: Quit the game")

def main():
    # Initial position of the Pokémon and screen size
    position_x, position_y = 10, 10
    width, height = 80, 24

    # List of available Pokémon (ASCII art)
    pokemon_list = [
        PIKACHU, BULBASAUR, CHARMANDER, EEVEE, 
        PSYDUCK, JIGGLYPUFF, MEOWTH, SNORLAX, 
        SQUIRTLE, MAGIKARP, CATERPIE, GENGAR, 
        CHARIZARD, RAICHU, ZUBAT, ONIX, 
        TOGEPI, SANDSHREW, ABRA, MACHOP, 
        ELECTRODE, VILEPLUME, LITTEN, RATTATA, 
        JOLTEON, VAPOREON, FLAREON, LEAFEON, 
        GLACEON, ESPEON, SILICOBRA, LUXRAY, 
        DRATINI, TROPIUS, LUGIA, HO_OH, 
        MILTANK, ZORUA, LEAVANNY, DARUMAKA, 
        EXCADRILL, WAILMER, CHEREN
    ]
    
    # Initial Pokémon index and the current Pokémon
    pokemon_index = 0
    current_pokemon = pokemon_list[pokemon_index]

    # Print the controls for the game
    print_controls()

    # Main game loop
    running = True
    while running:
        # Draw the game screen with the current Pokémon at the specified position
        draw_game_screen(current_pokemon, position_x, position_y, width, height)  
        
        # Ask the player to input a command
        command = input("Enter command (w/a/s/d/p/q): ").strip().lower()

        if command == "q":
            # Exit the game
            running = False
        elif command == "p":
            # Switch Pokémon
            print("Available Pokémon: ", ', '.join([pokemon.split()[0] for pokemon in pokemon_list]))  # Show Pokémon names
            pokemon_name = input("Enter the name of the Pokémon you wish to use: ").strip().capitalize()

            # Look for the Pokémon in the list
            if pokemon_name in POKEMON_ASCII:
                current_pokemon = POKEMON_ASCII[pokemon_name]
            else:
                print(f"Invalid Pokémon name '{pokemon_name}'. Try again.")
        elif command == 'w':
            position_y = max(1, position_y - 1)  # Move up
        elif command == 's':
            position_y = min(height - 2, position_y + 1)  # Move down
        elif command == 'a':
            position_x = max(1, position_x - 1)  # Move left
        elif command == 'd':
            position_x = min(width - 2, position_x + 1)  # Move right

    # Thank the player for playing when the game ends
    print('Thank you for playing!')

if __name__ == "__main__":
    # Run the main function
    main()
#edges, adding a progress bar.