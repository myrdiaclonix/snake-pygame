import pygame
import time
import random

snake_speed = 15

# Window size
x_size = 720
y_size = 480

# Defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((x_size, y_size))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# Defining snake status
snake_position = [100, 50]
snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]

fruit_position = [
    random.randrange(1, (x_size // 10)) * 10,
    random.randrange(1, (y_size // 10)) * 10
]
fruit_spawn = True

direction = 'RIGHT'
change_to = direction

# Initial score
score = 0

while True:
    pygame.display.update()