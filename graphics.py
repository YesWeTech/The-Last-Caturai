#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""graphics.py"""

"""
This file is part of The Last Caturai.

    The Last Caturai is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    The Last Caturai is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
"""

"""It handles graphics."""

import pygame
import config

BLACK    = (   0,   0,   0)

# Corta un chara en las fil y col indicadas. Array Bidimensional.
# tomada de: http://razonartificial.com/2010/06/engine-xi-creando-al-heroe/
def _cortar_chara(ruta, fil, col):
    image = load_image(ruta, True)
    rect = image.get_rect()
    w = rect.w / col
    h = rect.h / fil
    sprite = range(fil)
    for i in range(fil):
        sprite[i] = list(range(col))

    for f in range(fil):
        for c in range(col):
            sprite[f] = image.subsurface((rect.left, rect.top, w, h))
            rect.left += w
        rect.top += h
        rect.left = 0

    return sprite


def get_image(file_name, x, y, width, height):
    """ Grab a single image out of a larger spritesheet
        Pass in the x, y location of the sprite
        and the width and height of the sprite. """

    sprite_sheet = pygame.image.load(file_name).convert()

    # Create a new blank image
    image = pygame.Surface([width, height]).convert()

    # Copy the sprite from the large sheet onto the smaller image
    image.blit(sprite_sheet, (0, 0), (x, y, width, height))

    # Assuming black works as the transparent color
    image.set_colorkey(BLACK)

    # Return the image
    return image

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
        image.set_colorkey(color, pygame.RLEACCEL)
    return image

# Function to manage texts
def text(text, posx, posy, color, size):
    font = pygame.font.Font(config.fonts+"ShrimpFriedRiceNo1.ttf", size)
    output = pygame.font.Font.render(font, text, 1, color) # Transforms font into a Sprite
    output_rect = output.get_rect()
    output_rect.centerx = posx
    output_rect.centery = posy

    return output, output_rect
