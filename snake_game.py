"""
Snake game
"""

import pygame

pygame.init()
snake_display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake Game by Wellington College KFW')
game_over = False
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                game_over = True
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT:
                        x1_change = -10
                        y1_change = 0
                    case pygame.K_RIGHT:
                        x1_change = 10
                        y1_change = 0
                    case pygame.K_UP:
                        y1_change = -10
                        x1_change = 0
                    case pygame.K_DOWN:
                        y1_change = 10
                        x1_change = 0

    x1 += x1_change
    y1 += y1_change
    snake_display.fill(white)
    pygame.draw.rect(snake_display, black, [x1, y1, 10, 10])

    pygame.display.update()

    clock.tick(30)

pygame.quit()
