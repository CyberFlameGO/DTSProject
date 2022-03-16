"""
Work for when we are away
"""

from typing import Sequence, Union

import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame  # noqa: E402 isort: skip

DISPLAY_WIDTH: int = 1000
DISPLAY_HEIGHT: int = 1000
WHITE: tuple[int, int, int] = (255, 255, 255)
BLACK: tuple[int, int, int] = (0, 0, 0)
DEEP_RED: tuple[int, int, int] = (255, 0, 0)

pygame.init()

walk_count: int = 0
bg = pygame.image.load(r'./assets/bg.jpg')

display_surface: Union[pygame.Surface, pygame.SurfaceType] = pygame.display.set_mode(
    (DISPLAY_WIDTH, DISPLAY_HEIGHT)
)


def redraw_gamewindow():
    """
    Redraws the game window
    """
    global walk_count
    display_surface.blit(bg, (0, 0))
    pygame.display.update()


def main():
    """
    Main function
    """
    x: int = 0
    y: int = 400
    width: int = 64
    height: int = 64
    velocity: int = 5
    jumps: int = 10
    jumping: bool = False
    run: bool = True
    left: bool = False
    right: bool = False
    pygame.display.set_caption("dn")
    walk_right: list = [pygame.image.load(r'./assets/R1.png'), pygame.image.load(r'./assets/R2.png'),
                        pygame.image.load(r'./assets/R3.png'), pygame.image.load(r'./assets/R4.png'),
                        pygame.image.load(r'./assets/R5.png'), pygame.image.load(r'./assets/R6.png'),
                        pygame.image.load(r'./assets/R7.png'), pygame.image.load(r'./assets/R8.png'),
                        pygame.image.load(r'./assets/R9.png')]
    walk_left: list = [pygame.image.load(r'./assets/L1.png'), pygame.image.load(r'./assets/L2.png'),
                       pygame.image.load(r'./assets/L3.png'), pygame.image.load(r'./assets/L4.png'),
                       pygame.image.load(r'./assets/L5.png'), pygame.image.load(r'./assets/L6.png'),
                       pygame.image.load(r'./assets/L7.png'), pygame.image.load(r'./assets/L8.png'),
                       pygame.image.load(r'./assets/L9.png')]
    bg = pygame.image.load(r'./assets/bg.jpg')
    char = pygame.image.load(r'./assets/standing.png')
    playing: bool = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.KEYDOWN:
                pass
        keys: Sequence[bool] = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if x > velocity:
                x -= velocity
        if keys[pygame.K_RIGHT]:
            if x < DISPLAY_WIDTH - width - velocity:
                x += velocity
        if not jumping:
            if keys[pygame.K_SPACE]:
                jumping = True
                print("ok")
        else:
            while jumping:
                print("who")
                if jumps >= -10:
                    y -= (jumps * abs(jumps)) * 0.5
                    jumps -= 1
                else:
                    jumps = 10
                    jumping = False
                    print("sher")
        redraw_gamewindow()


class Player(object):
    """
    Player class oh yeah
    """
    pass


if __name__ == "__main__":
    main()
