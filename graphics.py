#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""graphics.py"""

"""It handles graphics."""

import pygame

# Function which loads an image into the Window
def load_image(path, transparent):
    try: image = pygame.image.load(path)
    # Manages error if image cannot be loaded
    except (pygame.error) as message:
        raise(message)
    # Converting to inner pygame format (more efficient)
    image = image.convert()
    if transparent:
        color = image.get_at((0, 0))
        image.set_colorkey(color, RLEACCEL)
    return image

# Function to manage texts
def text(text, posx, posy, color, size):
    font = pygame.font.Font(font_path, size)
    output = pygame.font.Font.render(font, text, 1, color) # Transforms font into a Sprite
    output_rect = output.get_rect()
    output_rect.centerx = posx
    output_rect.centery = posy

    return output, output_rect
