#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""character.py"""

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

"""Defines an abstract character"""

from graphics import load_image
import Physics

class Character(Physics):
    def __init__(self, hp, position, sprite):
        super(Character, self).__init__(position = position)
        self.hp = hp
        self.sprite = self._cortar_chara(ruta=sprite, fil=4, col=4)
        self.image = self.sprite[0][0]
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def attack(self):
        raise NotImplemented("Implement the atack in MainCharacter and Enemy")

    def movement(self):
        raise NotImplemented("Implement the atack in MainCharacter and Enemy")
