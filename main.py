# Imports
import pygame
# Initialize pygame
pygame.init()


# To set game window
WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong") # Setting the game title on the display window

# Event loop that displays the game window and draws something on it
def main():
    run = True


    while run:
        for event in pygame.event.get():
            if event .type == pygame.QUIT:
                run = False
                break
    pygame.quit()