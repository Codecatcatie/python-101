import os
import requests
from colorama import Fore, Style, init
from characters import *  # Your ASCII Pokémon art
import curses
import time

# Initialize colorama
init(autoreset=True)

# ASCII art dictionary
POKEMON_ASCII = {
    "Pikachu": PIKACHU, "Bulbasaur": BULBASAUR, "Charmander": CHARMANDER, "Eevee": EEVEE,
    "Psyduck": PSYDUCK, "Jigglypuff": JIGGLYPUFF, "Meowth": MEOWTH, "Snorlax": SNORLAX,
    "Squirtle": SQUIRTLE, "Magikarp": MAGIKARP, "Caterpie": CATERPIE, "Gengar": GENGAR,
    "Charizard": CHARIZARD, "Raichu": RAICHU, "Zubat": ZUBAT, "Onix": ONIX,
    "Togepi": TOGEPI, "Sandshrew": SANDSHREW, "Abra": ABRA, "Machop": MACHOP,
    "Electrode": ELECTRODE, "Vileplume": VILEPLUME, "Litten": LITTEN, "Rattata": RATTATA,
    "Jolteon": JOLTEON, "Vaporeon": VAPOREON, "Flareon": FLAREON, "Leafeon": LEAFEON,
    "Glaceon": GLACEON, "Espeon": ESPEON, "Silicobra": SILICOBRA, "Luxray": LUXRAY,
    "Dratini": DRATINI, "Tropius": TROPIUS, "Lugia": LUGIA, "Ho_oh": HO_OH,
    "Miltank": MILTANK, "Zorua": ZORUA, "Leavanny": LEAVANNY, "Darumaka": DARUMAKA,
    "Excadrill": EXCADRILL, "Wailmer": WAILMER, "Cheren": CHEREN
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_pokemon_data(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def format_stats_block(pokemon_data):
    if not pokemon_data:
        return ["Stats unavailable."]

    name = pokemon_data["name"].capitalize()
    pokemon_id = pokemon_data["id"]
    height = pokemon_data["height"] / 10
    weight = pokemon_data["weight"] / 10
    types = [t["type"]["name"].capitalize() for t in pokemon_data["types"]]
    abilities = [a["ability"]["name"].replace("-", " ").capitalize() for a in pokemon_data["abilities"]]

    lines = [
        f"=== {name} ===",
        f"ID       : {pokemon_id}",
        f"Height   : {height} m",
        f"Weight   : {weight} kg",
        f"Types    : {', '.join(types)}",
        f"Abilities: {', '.join(abilities)}",
        "",
        "Base Stats:"
    ]

    for stat in pokemon_data["stats"]:
        stat_name = stat["stat"]["name"].replace("-", " ").capitalize()
        stat_value = stat["base_stat"]
        bar = "#" * (stat_value // 5)
        lines.append(f"{stat_name:12}: {stat_value:3} |{bar}")

    return lines

def draw_combined_screen(pokemon_ascii, stats_block, pos_x, pos_y, width, height):
    clear_screen()

    # Create empty screen frame
    screen = []
    for i in range(height):
        if i == 0 or i == height - 1:
            screen.append("+" + (width - 2) * "-" + "+")
        else:
            screen.append("|" + (width - 2) * " " + "|")

    # Draw Pokémon ASCII into screen
    lines = pokemon_ascii.strip("\n").split("\n")
    for i, line in enumerate(lines):
        y = pos_y + i
        if 0 < y < height - 1:
            line_chars = list(screen[y])
            for j, char in enumerate(line):
                x = pos_x + j
                if 0 < x < width - 1 and char != " ":
                    line_chars[x] = char
            screen[y] = "".join(line_chars)

    # Append stats block to right side of each line
    for i in range(len(screen)):
        stat_line = stats_block[i] if i < len(stats_block) else ""
        screen[i] += "   " + stat_line

    # Print full combined screen
    for line in screen:
        print(line)

def print_controls():
    print("\nControls:")
    print("- w: Move up")
    print("- s: Move down")
    print("- a: Move left")
    print("- d: Move right")
    print("- p: Switch Pokémon")
    print("- q: Quit the game")

def main(stdscr):
    global current_pokemon_name

    # Set up curses
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    stdscr.timeout(100)  # Non-blocking input with 100ms timeout

    POKEMON_ASCII = {
        "Pikachu": PIKACHU, "Bulbasaur": BULBASAUR, "Charmander": CHARMANDER, "Eevee": EEVEE,
        "Psyduck": PSYDUCK, "Jigglypuff": JIGGLYPUFF, "Meowth": MEOWTH, "Snorlax": SNORLAX,
        "Squirtle": SQUIRTLE, "Magikarp": MAGIKARP, "Caterpie": CATERPIE, "Gengar": GENGAR,
        "Charizard": CHARIZARD, "Raichu": RAICHU, "Zubat": ZUBAT, "Onix": ONIX,
        "Togepi": TOGEPI, "Sandshrew": SANDSHREW, "Abra": ABRA, "Machop": MACHOP,
        "Electrode": ELECTRODE, "Vileplume": VILEPLUME, "Litten": LITTEN, "Rattata": RATTATA,
        "Jolteon": JOLTEON, "Vaporeon": VAPOREON, "Flareon": FLAREON, "Leafeon": LEAFEON,
        "Glaceon": GLACEON, "Espeon": ESPEON, "Silicobra": SILICOBRA, "Luxray": LUXRAY,
        "Dratini": DRATINI, "Tropius": TROPIUS, "Lugia": LUGIA, "Ho_oh": HO_OH,
        "Miltank": MILTANK, "Zorua": ZORUA, "Leavanny": LEAVANNY, "Darumaka": DARUMAKA,
        "Excadrill": EXCADRILL, "Wailmer": WAILMER, "Cheren": CHEREN
    }
    current_pokemon_name = "Pikachu"
    current_pokemon = POKEMON_ASCII[current_pokemon_name]

    position_x, position_y = 10, 5
    width, height = 80, 24
    #height, width = stdscr.getmaxyx()

    # pokemon_names = list(POKEMON_ASCII.keys())
    # current_name = pokemon_names[0]
    # current_ascii = POKEMON_ASCII[current_name]
    # pokemon_data = get_pokemon_data(current_name)
    # stats_block = format_stats_block(pokemon_data)
    #print_controls()

    # Main game loop
    running = True
    while running:
        stdscr.clear()

        current_pokemon = POKEMON_ASCII[current_pokemon_name]
        pokemon_lines = current_pokemon.split("\n")
        pokemon_width = max(len(line) for line in pokemon_lines)
        pokemon_height = len(pokemon_lines)
      
#       # # aw border
        for y in range(height-1):
            if y == 0 or y == height-2:
                stdscr.addstr(y, 0, "+" + "-" * (width-2) + "+")
            else:
                stdscr.addstr(y, 0, "|")
                stdscr.addstr(y, width-1, "|")

         # Draw the Pokémon
        for i, line in enumerate(pokemon_lines):
            if 0 <= position_y + i < height-2:
                stdscr.addstr(position_y + i, position_x, line)

        # Draw info bar
        stdscr.addstr(height-1, 0, f"Current Pokémon: {current_pokemon_name} | Use W/A/S/D to move, P to switch, Q to quit")

        # Get user input (non-blocking)
        key = stdscr.getch()

        if key == ord('q'):
            running = False
        elif key == ord('p'):
            # Cycle through Pokémon
            pokemon_names = list(POKEMON_ASCII.keys())
            current_index = pokemon_names.index(current_pokemon_name)
            current_pokemon_name = pokemon_names[(current_index + 1) % len(pokemon_names)]
            print("Available Pokémon:", ", ".join(pokemon_names))
        elif key == ord('w'):
            position_y = max(1, position_y - 1)
        elif key == ord('s'):
            position_y = min(height - pokemon_height - 3, position_y + 1)
        elif key == ord('a'):
            position_x = max(1, position_x - 1)
        elif key == ord('d'):
            position_x = min(width - pokemon_width - 2, position_x + 1)

        # Refresh the screen
        stdscr.refresh()

        # Small delay
        time.sleep(0.05)

    
    print("Thanks for playing!")

if __name__ == "__main__":
    current_pokemon_name = ""
    curses.wrapper(main)




    
#   elif command == "p":
#             print("Available Pokémon:", ", ".join(pokemon_names))
#             new_name = input("Enter Pokémon name: ").strip().capitalize()
#             if new_name in POKEMON_ASCII:
#                 current_name = new_name
#                 current_ascii = POKEMON_ASCII[new_name]
#                 pokemon_data = get_pokemon_data(new_name)
#                 stats_block = format_stats_block(pokemon_data)
#             else:
#                 print("Invalid name.")