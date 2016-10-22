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

import Physics, pygame, constants
from graphics import load_image

class Character(Physics):
    def __init__(self, hp, position, sprite):
        super(Character, self).__init__(position = position)
        self.hp = hp
        self.sprite = self._cortar_chara(ruta=sprite, fil=4, col=4)
        self.image = self.sprite[0][0]
        self.rect = self.image.get_rect()

    # Corta un chara en las fil y col indicadas. Array Bidimensional.
    # tomada de: http://razonartificial.com/2010/06/engine-xi-creando-al-heroe/
    def _cortar_chara(self, ruta, fil, col):
        image = load_image(ruta, True)
        rect = image.get_rect()
        w = rect.w / col
        h = rect.h / fil
        sprite = range(fil)
        for i in range(fil):
            sprite[i] = range(col)

        for f in range(fil):
            for c in range(col):
                sprite[f] = image.subsurface((rect.left, rect.top, w, h))
                rect.left += w
            rect.top += h
            rect.left = 0

        return sprite

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def attack(self):
        raise NotImplemented("Implement the atack in MainCharacter and Enemy")

    def movement(self):
        raise NotImplemented("Implement the atack in MainCharacter and Enemy")

    def jump(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.__position_y__ = -10