# -*- coding: utf-8 -*-
"""
Work for when we are away
"""

from typing import Union

import pygame


DISPLAY_WIDTH: int = 640
DISPLAY_HEIGHT: int = 480
WHITE = (255, 255, 255)

display_surface: Union[pygame.Surface, pygame.SurfaceType] = pygame.display.set_mode(
    (DISPLAY_WIDTH, DISPLAY_HEIGHT)
)
image = pygame.image.load(r'dn.gif')
pygame.display.set_caption("dn")
mario_x: int = 0
mario_y: int = 0

playing: bool = True
while playing:
    display_surface.fill(WHITE)
    mario = display_surface.blit(image, (mario_x, mario_y))
    transit: bool = False
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                playing = False
            case pygame.MOUSEBUTTONDOWN:
                # Check if left click
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    x, y = pygame.mouse.get_pos()
                    if image.get_rect().collidepoint(x, y):
                        print(u"printing dn")
                        transit = True
    if transit:
        mario_y -= 10

    pygame.display.update()
