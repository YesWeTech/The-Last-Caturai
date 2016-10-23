#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""platform.py"""

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

"""Creates and manages platforms."""

import pygame
import tile

GRASS_UP = (196, 196, 196, 196)
GRASS_DOWN = (196, 588, 196, 196)
STONE_UP = (392, 196, 196, 196)
STONE_DOWN = (0, 196, 196, 196)

class Platform(pygame.sprite.Sprite):

    def __init__(self, tile_sheet_data):

        pygame.sprite.Sprite.__init__(self)

        tile_sheet = SpriteSheet("tileset.jpg")
        self.image = tile_sheet.get_image(tile_sheet_data[0], tile_sheet_data[1], tile_sheet_data[2], tile_sheet_data[3])

        self.rect = self.image.get_rect()


class MovingPlatform(Platform):

    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    level = None
    player = None

    def update(self):

        # Moving the platform left and right
        self.rect.x += self.change_x

        # As the platform: am I hitting the player?
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                self.player.rect.left = self.rect.right

        # Moving the platform up and down
        self.rect.y += self.change_y

        # As the platform: am I hitting the player?
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit: # Same
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
