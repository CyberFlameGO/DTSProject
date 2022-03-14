"""
Work for when we are away
"""

from typing import Union

import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame  # noqa: E402

DISPLAY_WIDTH: int = 500
DISPLAY_HEIGHT: int = 500
WHITE = (255, 255, 255)

pygame.init()

display_surface: Union[pygame.Surface, pygame.SurfaceType] = pygame.display.set_mode(
    (DISPLAY_WIDTH, DISPLAY_HEIGHT)
)
pygame.display.set_caption("dn")
x: int = 0
y: int = 0

width: int = 40
height: int = 60
velocity: int = 5


def main():
    """
    Main function
    """
    pygame.display.set_caption("dn")
    playing: bool = True
    while playing:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    playing = False
                    continue
                case pygame.MOUSEBUTTONDOWN:
                    # Check if left click
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        x, y = pygame.mouse.get_pos()
                        if image.get_rect().collidepoint(x, y):
                            print(u"printing dn")
            pygame.display.update()


if __name__ == "__main__":
    main()
