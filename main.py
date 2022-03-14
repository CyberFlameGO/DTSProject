"""
Work for when we are away
"""

from typing import Union

import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame  # noqa: E402

DISPLAY_WIDTH: int = 500
DISPLAY_HEIGHT: int = 500
WHITE: tuple[int, int, int] = (255, 255, 255)
BLACK: tuple[int, int, int] = (0, 0, 0)
DEEP_RED: tuple[int, int, int] = (255, 0, 0)

pygame.init()

display_surface: Union[pygame.Surface, pygame.SurfaceType] = pygame.display.set_mode(
    (DISPLAY_WIDTH, DISPLAY_HEIGHT)
)


def main():
    """
    Main function
    """
    x: int = 0
    y: int = 0
    width: int = 40
    height: int = 60
    velocity: int = 5
    jumps: int = 0
    jumping: bool = False
    pygame.display.set_caption("dn")
    playing: bool = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            elif event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT:
                        if x > velocity:
                            x -= velocity
                    case pygame.K_RIGHT:
                        if x < DISPLAY_WIDTH - width - velocity:
                            x += velocity
                    case pygame.K_UP:
                        if y > velocity and not jumping:
                            y -= velocity
                    case pygame.K_DOWN:
                        if y < DISPLAY_HEIGHT - height - velocity and not jumping:
                            y += velocity
                    case pygame.K_SPACE:
                        if not jumping:
                            jumping = True
            else:
                while jumping:
                    if jumps >= -10:
                        y -= (jumps * abs(jumps)) * 0.5
                        jumps -= 1
                    else:
                        jumps = 10
                        jumping = False
                display_surface.fill(BLACK)
            red_rectangle = pygame.draw.rect(display_surface, DEEP_RED, (x, y, width, height))
            pygame.display.update()


if __name__ == "__main__":
    main()
