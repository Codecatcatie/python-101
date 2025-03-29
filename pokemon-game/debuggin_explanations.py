import os  # Importing the OS module to clear the terminal screen

def clear_screen():
    os.system('clear')  # Clears the terminal screen using the clear command

def draw_game_screen(pokemon, position_x, position_y, width, height):
    # Initialize an empty screen with spaces for each row
    screen = [" " * width for _ in range(height)]

    # Draw the top and bottom borders of the screen
    for i in range(height):
        if i == 0 or i == height - 1:  # Top or Bottom border
            screen[i] = "+" + "-" * (width - 2) + "+"  # Border with '+' at ends and '-' in between
        else:  # Left and right border with spaces in between
            screen[i] = "|" + " " * (width - 2) + "|"

    # Split the Pokémon ASCII art into individual lines
    lines = pokemon.split("\n")

    # Loop through each line of the Pokémon
    for i, line in enumerate(lines):
        y_pos = position_y + i  # Calculate the vertical position on the screen
        if 0 < y_pos < height - 1:  # Check if it's within the screen bounds (not on the border)
            screen_line = list(screen[y_pos])  # Convert the line into a list to modify characters

            # Check if it's the first line, and shift it 2 spaces to the right
            shift = 2 if i == 0 else 0  # Only shift the first line by 2 spaces to the right

            # Loop through each character in the Pokémon's current line
            for j, char in enumerate(line):
                x_pos = position_x + j + shift  # Calculate the horizontal position (add shift for the first line)
                if 0 < x_pos < width - 1 and char != " ":  # Ensure we stay within the screen's boundaries
                    screen_line[x_pos] = char  # Insert the character at the correct position

            screen[y_pos] = "".join(screen_line)  # Join the modified list back into a string and update the screen

    clear_screen()  # Clear the screen before printing the updated version
    print("\n".join(screen))  # Print the full screen with all the lines

# Test Run: Display the CHARMANDER Pokémon at (10, 5) on a 80x24 screen
if __name__ == "__main__":
    from characters import CHARMANDER  # Import the CHARMANDER ASCII art from characters.py
    draw_game_screen(CHARMANDER, 10, 5, 80, 24)  # Call the function to display the game screen
