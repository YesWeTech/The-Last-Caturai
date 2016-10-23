#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""enemy.py"""

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

"""It defines the general enemies of the game."""

from Character import Character
import pygame

class Enemy(Character):
    def __init__(self, hp, position, sprite):
        super(Enemy, self).__init__(hp, position, sprite)

    def attack(self):
        pass

    def movement(self):
        pass
