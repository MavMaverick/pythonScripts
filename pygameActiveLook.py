import pygame
import sys

def split_string_at_space(text, max_char_limit):
    """
    Splits a string into two parts: a line of specified max length, wrapping at spaces, 
    and the remaining text. Long words exceeding max length are hyphenated.

    Parameters:
    - text (str): The input string to be wrapped.
    - max_char_limit (int): The maximum number of characters per line.

    Returns:
    - tuple (str, str): A line wrapped to fit within the specified length, and the remaining text.

    Example:
    >>> split_string_at_space("This is a sample string that needs to be split.", 10)
    ("This is a", "sample string that needs to be split.")
    """
    
    text_length = len(text) # Calculate text length once to reduce calculations

    # If the text length is within the limit, return it as-is 
    if text_length <= max_char_limit:
        return text, ""

    # If the next character after max_char_limit's index is a " "
    if text[max_char_limit] == " ":
        return text[0:max_char_limit], text[max_char_limit + 1:]

    # If max_char_limit isn't a space, search backwards for the nearest space
    curr_index = max_char_limit - 2
    while curr_index > 0 and text[curr_index] != " ":
        curr_index -= 1

    # If curr_index is zero, the word exceeds max length and should be split with a hyphen
    # Example: If max_char_limit = 29, and text is 'supercalifragilisticexpialidocious', 
    #          split into ['supercalifragilisticexpiali-', 'docious']
    if curr_index == 0:
         return text[0:max_char_limit - 1]+'-', text[max_char_limit - 1:]

    # Return everything up to the space (but not space), and everything after space.
    else:
         return text[0:curr_index], text[curr_index + 1:]
        
# words = "This is a sample text to demonstrate the monospace lens line-breaking algorithm."
words = "This is a sample text to demonstrate the monospace supercalifragilisticexpialidocious lens line-breaking algorithm. I have extended this string to further test the capability of the line breaking. It seems to be working well, which is very good. Hopefully."
char_screen_len = 29

# Split the text into multiple lines
lines = []
while words:
    line, words = split_string_at_space(words, char_screen_len)
    lines.append(line)

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 244
# screen_width = 600
screen_height = 206
# screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Text on Screen')

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)  # RGB for yellow

# Set up the monospace font
font = pygame.font.SysFont('Monaco', 24)

# UI elements 
battery = '100%'
divider = '__________________________'

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(black)

    # Render and display each line of text
    y_offset = 24
    for line in lines:
        text_surface = font.render(line, True, yellow)
        screen.blit(text_surface, (10, y_offset))  # Display at coordinates (10, y_offset)
        y_offset += font.get_height() + 5  # Move down for the next line


    # UI Elements, don't touch
    text_surface1 = font.render(battery, True, yellow)
    screen.blit(text_surface1, (180, 1))  # Display at coordinates (10, 10)
    text_surface2 = font.render(divider, True, yellow)
    screen.blit(text_surface2, (5, 2))  # Display at coordinates (10, 10)

    # Update the display
    pygame.display.flip()


# Quit Pygame
pygame.quit()
sys.exit()
