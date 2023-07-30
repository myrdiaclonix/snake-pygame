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

# Displaying score


def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()

    game_window.blit(score_surface, score_rect)

# Game over function


def game_over():
    my_font = pygame.font.SysFont('sitkabanner', 50)
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()

    # Set position of the text
    game_over_rect.midtop = (x_size / 2, y_size / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # Quit the program after 2 seconds
    time.sleep(2)

    # Deactive pygame library
    pygame.quit()

    quit()


while True:
    # Key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Prevent snake go to oposite directions
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (x_size // 10)) * 10,
                          random.randrange(1, (y_size // 10)) * 10]

    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # Game over rules
    if snake_position[0] < 0 or snake_position[0] > x_size - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > y_size - 10:
        game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(white, 'sitkabanner', 20)

    # Refresh game screen
    pygame.display.update()
    fps.tick(snake_speed)
