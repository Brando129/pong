# Imports
import pygame
# Initialize pygame
pygame.init()

# Set game window
WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong") # Setting the game title on the display window

FPS = 60 # Frames per second
# Color values
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Classes

# Paddle class
class Paddle:
    COLOR = WHITE

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y , self.width, self.height))

# Draw function
def draw(win): # win stands for (game window)
    win.fill(BLACK) # Window color
    pygame.display.update() # Update the game window (This should only be done after all the drawing is done)

# Event function that displays the game window and draws something on it
def main():
    run = True
    clock = pygame.time.Clock() # Regulate the frame rate of our game

    # Main event loop
    while run:
        clock.tick(FPS)
        draw(WIN) # Window that we want to draw on

        for event in pygame.event.get():
            if event .type == pygame.QUIT:
                run = False
                break
    pygame.quit()

# Ensure that we are running this module to call the main function
if __name__ == '__main__':
    main()