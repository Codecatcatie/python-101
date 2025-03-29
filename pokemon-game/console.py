import os

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
    lines = pokemon.strip().split("\n")
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
    current_pokemon = CHARMANDER

    draw_game_screen(current_pokemon, position_x, position_y, width, height)
    print('Thank you for playing!')
    
if __name__ == "__main__":
    main()

