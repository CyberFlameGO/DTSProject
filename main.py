"""
Work for when we are away
"""

from typing import Sequence, Union

import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame  # noqa: E402 isort: skip

DISPLAY_WIDTH: int = 500
DISPLAY_HEIGHT: int = 500
WHITE: tuple[int, int, int] = (255, 255, 255)
BLACK: tuple[int, int, int] = (0, 0, 0)
DEEP_RED: tuple[int, int, int] = (255, 0, 0)

pygame.init()
clock = pygame.time.Clock()
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
walk_count: int = 0
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

display_surface: Union[pygame.Surface, pygame.SurfaceType] = pygame.display.set_mode(
    (DISPLAY_WIDTH, DISPLAY_HEIGHT)
)


class Player(object):
    """
    Player class oh yeah
    """

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.jumps: int = 10
        self.jumping: bool = False
        self.run: bool = True
        self.left: bool = False
        self.right: bool = False
        self.walk_count: int = 0
        self.bounding_box = (self.x + 17, self.y + 10, 28, 52)

    def draw(self, window):
        """
        Draw
        :param window:
        """


def redraw_game_window():
    """
    Redraws the game window
    """
    global walk_count, left, right
    display_surface.blit(bg, (0, 0))
    if walk_count + 1 >= 27:
        walk_count = 0
    if left:
        display_surface.blit(walk_left[walk_count // 3], (x, y))
        walk_count += 1
    elif right:
        display_surface.blit(walk_right[walk_count // 3], (x, y))
        walk_count += 1
    else:
        display_surface.blit(char, (x, y))
        walk_count = 0
    pygame.display.update()


def main():
    """
    Main function
    """
    player_character = Player(300, 410, 64, 64)
    global x, y, width, height, velocity, jumps, jumping, run
    pygame.display.set_caption("dn")
    playing: bool = True
    while playing:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.KEYDOWN:
                pass
        keys: Sequence[bool] = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if player_character.x > player_character.velocity:
                player_character.x -= player_character.velocity
                player_character.left = True
                player_character.right = False
        elif keys[pygame.K_RIGHT]:
            if player_character.x < DISPLAY_WIDTH - player_character.width - player_character.velocity:
                player_character.x += player_character.velocity
                player_character.left = False
                player_character.right = True

        else:
            player_character.left, player_character.right = False, False
        if not player_character.jumping:
            if keys[pygame.K_SPACE]:
                player_character.jumping = True
                player_character.left, player_character.right = False, False
                player_character.walk_count = 0
                print("ok")
        else:
            if player_character.jumps >= -10:
                negative = 1
                print("who")
                if player_character.jumps < 0:
                    negative = -1
                player_character.y -= (player_character.jumps ** 2) * 0.5 * negative
                player_character.jumps -= 1

            else:
                player_character.jumps = 10
                player_character.jumping = False
                print("sher")
        redraw_game_window()


if __name__ == "__main__":
    main()
