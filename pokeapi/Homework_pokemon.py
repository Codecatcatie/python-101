import requests
import json
from colorama import Fore, Style, init

init()

def get_pokemon_data(pokemon_name):
    """
    Get information about a specific Pokémon.
    Returns the full response data or None if not found.
    """
    print(f"Searching for {Fore.YELLOW}{pokemon_name}{Style.RESET_ALL}...")
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    
     # Check if the request was successful
    if response.status_code == 200:
        print(f"{Fore.GREEN}Pokémon {pokemon_name} found!{Style.RESET_ALL}")
        return response.json()
    else:
        print(f"{Fore.RED}Request failed with status code {response.status_code}{Style.RESET_ALL}")
        return None

def display_pokemon_basic_info(pokemon_data):
    """Display basic information about a Pokémon in a formatted way."""
    if not pokemon_data:
        return
    
    # Get basic information
    name = pokemon_data["name"].capitalize()
    pokemon_id = pokemon_data["id"]
    height = pokemon_data["height"] / 10  # Convert to meters
    weight = pokemon_data["weight"] / 10  # Convert to kg
    
    # Get types
    types = [t["type"]["name"].capitalize() for t in pokemon_data["types"]]
    
    # Get abilities
    abilities = [a["ability"]["name"].replace("-", " ").capitalize() 
                 for a in pokemon_data["abilities"]]
    
    # Display information
    print(f"\n{Fore.CYAN}===== {name} ====={Style.RESET_ALL}")
    print(f"Pokédex ID: {pokemon_id}")
    print(f"Height: {height} m")
    print(f"Weight: {weight} kg")
    print(f"Types: {', '.join(types)}")
    print(f"Abilities: {', '.join(abilities)}")
    
    # Get and display base stats
    print(f"\n{Fore.CYAN}Base Stats:{Style.RESET_ALL}")
    for stat in pokemon_data["stats"]:
        stat_name = stat["stat"]["name"].replace("-", " ").capitalize()
        stat_value = stat["base_stat"]
        print(f"  {stat_name}: {stat_value}")
def explore_pokemon_moves(pokemon_moves):
    if not pokemon_moves:
        return 

    level_up_moves = []
    seen_moves = set()  # To track unique (name, level) pairs

    for move in pokemon_moves:
        
        #print(f"\nMove: {move["move"]["name"]}")

         # Only consider level-up moves from the latest game version
        for version_detail in move["version_group_details"]:
           if version_detail["move_learn_method"]["name"] == "level-up":
               move_name = move["move"]["name"]
               move_level = version_detail["level_learned_at"]
               # Check for duplicates before appending
               if (move_name, move_level) not in seen_moves:
                   level_up_moves.append({
                      "name": move_name,
                      "level": move_level
                   })
                   seen_moves.add((move_name, move_level))  # Add to seen

    # lambda arguments: expression (doesn't need def , you can write it right in place). Starts with thekey word landa(instead of def) then the argument, then the body.
    # 
    # add = lambda x, y: x + y
    # 
    # it equals to:
    # 
    # def add(x, y)
    #   return x + y   
    # 
    # uppercase = lambda text: text.upper()  
    # print(uppercase("hello"))  # Output: "HELLO"

    level_up_moves.sort(key=lambda x: x["level"])  # Sort by level (lowest first)    


    # NEW: Nicely formatted output

    for move in level_up_moves:  # Loop through each move
        print(f"Move name: {move['name']}")  # Print move name
        print(f"Move level: {move['level']}")  # Print move level
        print("")  # Line break between moves

    print(f"\nTotal moves available: {len(pokemon_moves)}")
    return pokemon_moves
#pokemon = input("\nEnter Pokémon name: ")
#pokemon_data = get_pokemon_data(pokemon)
#display_pokemon_basic_info(pokemon_data)

pokemon = 'pikachu'
pokemon_data = get_pokemon_data(pokemon)
moves = explore_pokemon_moves(pokemon_data["moves"])
#print(moves)
 

#mew
#arceus
# Pikachu
# Charizard
# Bulbasaur
# Squirtle
# Eevee
# Jigglypuff
# Mewtwo
# Snorlax
# Gengar
# Gyarados . control + / = pip