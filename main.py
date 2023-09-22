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
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 7

# Classes

# Paddle class
class Paddle:
    # Class attributes apply to all instances of the class
    COLOR = WHITE
    VEL = 4

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y , self.width, self.height))

    # Move the paddle up and down
    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

# Ball class
class Ball:
    # Class attributes
    MAX_VEL = 5
    COLOR = WHITE

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    # Draw the pong ball
    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

# Draw function
def draw(win, paddles, ball): # win stands for (game window)
    win.fill(BLACK) # Window color

    # Draw both paddles
    for paddle in paddles:
        paddle.draw(win)

    # Draw line down the center of the window
    for i in range(10, HEIGHT, HEIGHT // 20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH // 2 - 5, i, 10, HEIGHT // 20))

    ball.draw(win)
    pygame.display.update() # Update the game window (This should only be done after all the drawing is done)


# Ball collision logic
def handle_collision(ball, left_paddle, right_paddle):
    # Ceiling/floor logic
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    # X axis
    # Collision with left paddle
    if ball.x_vel < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1

    # Collision with right paddle
    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1

# Paddle Movement
def handle_paddle_movement(keys, left_paddle, right_paddle):
    # Left Paddle
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)

    # Right Paddle
    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)


# Event function that displays the game window and draws something on it
def main():
    run = True
    clock = pygame.time.Clock() # Regulate the frame rate of our game

    # Paddle instances
    left_paddle = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

    # Ball instance
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)


    # Main event loop
    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle], ball) # Window that we want to draw on

        for event in pygame.event.get():
            if event .type == pygame.QUIT:
                run = False
                break


        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        ball.move()
        handle_collision(ball, left_paddle, right_paddle)

    pygame.quit()

# Ensure that we are running this module to call the main function
if __name__ == '__main__':
    main()