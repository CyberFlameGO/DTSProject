"""
SNEKSY GAME
"""
import collections
from typing import Union

import pygame
from random import randint

FOOD_SIZE: int = 10
DISPLAY_WIDTH: int = 640
DISPLAY_HEIGHT: int = 480
BG_COLOR: tuple[int, int, int] = (44, 62, 80)
SNAKE_COLOR: tuple[int, int, int] = (236, 240, 241)
FOOD_COLOR: tuple[int, int, int] = (241, 196, 15)


def draw_food(display: pygame.Surface | pygame.SurfaceType, coords: collections.Iterable) -> object:
    """
    Draw food
    :param display:
    :param coords:
    :return:
    """
    new_food_list: list[Union[pygame.Rect, pygame.RectType]] = []
    pair: object
    for pair in coords:
        new_food_list.append(pygame.draw.rect(display,
                                              FOOD_COLOR,
                                              (pair[0],
                                               pair[1],
                                               FOOD_SIZE, FOOD_SIZE)))
    return new_food_list


def new_food():
    """
    Food gen
    :return:
    """
    new_x: int = randint(0, DISPLAY_WIDTH - 1) // FOOD_SIZE * FOOD_SIZE
    new_y: int = randint(0, DISPLAY_HEIGHT - 1) // FOOD_SIZE * FOOD_SIZE
    return [new_x, new_y]


def main():
    pygame.init()
    pygame.display.set_caption("Snakesy")
    clock: pygame.Clock = pygame.time.Clock()
    snake_display: Union[pygame.Surface, pygame.SurfaceType] = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    pygame.display.update()

    # generate food
    food_coordinates: list[list[int]] = []
    # for i in range(4):
    #     new_x = randint(0, DISPLAY_WIDTH - 1) // FOOD_SIZE * FOOD_SIZE
    #     new_y = randint(0, DISPLAY_HEIGHT - 1) // FOOD_SIZE * FOOD_SIZE
    #     food_coordinates.append([new_x, new_y])
    # print(food_coordinates)

    score: int = 0

    snake_x: float = DISPLAY_WIDTH / 2
    snake_y: float = DISPLAY_HEIGHT / 2
    snake_rectangle: pygame.Rect = pygame.Rect(snake_x, snake_y, FOOD_SIZE, FOOD_SIZE)
    snake_x_change: int = FOOD_SIZE
    snake_y_change: int = 0
    game_over = False
    while not game_over:
        if len(food_coordinates) == 0:
            food_coordinates.append(new_food())
        clock.tick(25)
        snake_display.fill(BG_COLOR)

        snake: Union[pygame.Rect, pygame.RectType] = pygame.draw.rect(snake_display, SNAKE_COLOR, snake_rectangle)
        food_list: Union[pygame.Rect | any | object] = draw_food(snake_display, food_coordinates)
        pygame.display.update()
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    game_over = True
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_LEFT:
                            snake_x_change = -FOOD_SIZE
                            snake_y_change = 0
                        case pygame.K_RIGHT:
                            snake_x_change = FOOD_SIZE
                            snake_y_change = 0
                        case pygame.K_UP:
                            snake_x_change = 0
                            snake_y_change = -FOOD_SIZE
                        case pygame.K_DOWN:
                            snake_x_change = 0
                            snake_y_change = FOOD_SIZE

        snake_rectangle: object = snake_rectangle.move(snake_x_change, snake_y_change)
        if snake.x < 0:
            snake_rectangle.update(DISPLAY_WIDTH - FOOD_SIZE, snake.y, FOOD_SIZE, FOOD_SIZE)
        elif snake.x > DISPLAY_WIDTH - FOOD_SIZE:
            snake_rectangle.update(0, snake.y, FOOD_SIZE, FOOD_SIZE)
        elif snake.y < 0:
            snake_rectangle.update(snake.x, DISPLAY_HEIGHT - FOOD_SIZE, FOOD_SIZE, FOOD_SIZE)
        elif snake.y > DISPLAY_WIDTH - FOOD_SIZE:
            snake_rectangle.update(snake.x, 0, FOOD_SIZE, FOOD_SIZE)

        if snake.collidelist(food_list) >= 0:
            food_coordinates.pop(snake.collidelist(food_list))
            score += 1
            print(score)


if __name__ == "__main__":
    main()
