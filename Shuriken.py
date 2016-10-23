#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Shuriken.py"""

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

"""It defines the objects used by the enemies to attack."""

from Physics import Physics
import pygame

class Shuriken(Physics):
    def __init__(self, img_path, position):
        super(Shuriken, self).__init__(img_path=img_path, position=position)
        self.direction = 'I'
        self.velocity = 1

    def draw(self, screen):
        screen.blit(self.image, self.position)

    def update(self):
        self.rect.x += self.x_speed_vector_
        aux = list(self.position)
        aux[0] = self.rect.x
        self.position = aux
        self.rect.y += self.y_speed_vector_

        # self.index = ((self.rect.x + self.world_shift + self.change_index) // 30) % 3

        # self.position = (self.rect.x, self.rect.y)
