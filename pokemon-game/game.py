import os
import requests
from colorama import Fore, Style, init
from characters import *  # Your ASCII Pokémon art
import curses
import time

# Initialize colorama
init(autoreset=True)

# # ASCII art dictionary
# POKEMON_ASCII = {
#     "Pikachu": { character: PIKACHU, color: 2, sound: 1 },

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

def main(stdscr):
    global current_pokemon_name

    # Set up colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)   # Border
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK) # Pikachu
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Bulbasaur
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)    # Charmander
    curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)   # Info text

    # Set up curses
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    stdscr.timeout(100)  # Non-blocking input with 100ms timeout

    current_pokemon_name = "Pikachu"
    current_pokemon = POKEMON_ASCII[current_pokemon_name]

    position_x, position_y = 10, 5
    width, height = 80, 24

    # Main game loop
    running = True
    while running:
        stdscr.clear()

        current_pokemon = POKEMON_ASCII[current_pokemon_name]
        pokemon_lines = current_pokemon.split("\n")
        pokemon_width = max(len(line) for line in pokemon_lines)
        pokemon_height = len(pokemon_lines)
      
#         Draw border
        for y in range(height-1):
            if y == 0 or y == height-2:
                stdscr.addstr(y, 0, "+" + "-" * (width-2) + "+", curses.color_pair(1))
            else:
                stdscr.addstr(y, 0, "|", curses.color_pair(1))
                stdscr.addstr(y, width-1, "|", curses.color_pair(1))

         # Draw the Pokémon
        for i, line in enumerate(pokemon_lines):
            if 0 <= position_y + i < height-2:
                stdscr.addstr(position_y + i, position_x, line, curses.color_pair(2))

        # Draw info bar
        stdscr.addstr(height-1, 0, f"Current Pokémon: {current_pokemon_name} | Use W/A/S/D to move, P to switch, Q to quit", curses.color_pair(5))

        # Draw stats
        #stats_block = format_stats_block(pokemon_data)
        #for line in stats_block:
        #    stdscr.addstr(line)

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
