


# # import os

# def clear_screen():
#     os.system('clear')

# def draw_game_screen(width, height):
#     screen = [" " * width for _ in range(height)]
    
#     for i in range(height):
#         if i == 0 or i == height - 1:
#             screen[i] = "+" + "-" * (width - 2) + "+"
#         else:
#             screen[i] = "|" + " " * (width - 2) + "|"

#     clear_screen()
#     for line in screen:
#         print(line)
import os

def clear_screen():
    os.system('clear')

def draw_game_screen(pokemon, position_x, position_y, width, height):
    screen = [" " * width for _ in range(height)]

    for i in range(height):
        if i == 0 or i == height - 1:
            screen[i] = "+" + "-" * (width - 2) + "+"
        else:
            screen[i] = "|" + " " * (width - 2) + "|"

    # Split Pokémon art into lines without stripping spaces
    lines = pokemon.split("\n")

    for i, line in enumerate(lines):
        y_pos = position_y + i
        if 0 < y_pos < height - 1:
            screen_line = list(screen[y_pos])
            
            #  Shift the first line  2 spaces to the right
            shift = 2 if i == 0 else 0  
            for j, char in enumerate(line):
                x_pos = position_x + j + shift  # Apply shift only to the first line
                
                if 0 < x_pos < width - 1 and char != " ":
                    screen_line[x_pos] = char
            
            screen[y_pos] = "".join(screen_line)

    clear_screen()
    print("\n".join(screen))

# Test Run
if __name__ == "__main__":
    from characters import BULBASAUR  # Ensure CHARMANDER is defined in characters.py
    draw_game_screen(BULBASAUR, 10, 5, 80, 24)