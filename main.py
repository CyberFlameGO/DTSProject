"""
Work for when we are away
"""

from typing import Union

import pygame


DISPLAY_WIDTH: int = 640
DISPLAY_HEIGHT: int = 480
WHITE = (255, 255, 255)
# TODO: Take a look at pygame fast-event

display_surface: Union[pygame.Surface, pygame.SurfaceType] = pygame.display.set_mode(
    (DISPLAY_WIDTH, DISPLAY_HEIGHT)
)
image = pygame.image.load(r'dn.gif')
pygame.display.set_caption("dn")

playing: bool = True
while playing:
    display_surface.fill(WHITE)
    mario = display_surface.blit(image, (0, 0))
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                playing = False
            case pygame.MOUSEBUTTONDOWN:
                print("nya")
                x, y = pygame.mouse.get_pos()
                if image.get_rect().collidepoint(x, y):
                    print(u"printing dn")
    pygame.display.update()
