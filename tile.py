#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""tile.py"""

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

"""Selects tiles from a tilesheet."""

import pygame
import config

class Tile(object):
    tile_sheet = None

    def __init__(self, filename):

        # Loading the tile sheet (196x196)
        self.tile_sheet = pygame.image.load(config.sprites+filename).convert()


    def get_image(self, x, y, width, height):

        image = pygame.Surface([width, height]).convert()
        image.blit(self.tile_sheet, (0, 0), (x, y, width, height))

        #color = image.get_at((0, 0))
        image.set_colorkey((0, 0, 0))

        return image
