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

from Physics import Physics
# import constants # => neccesary for jump method
# import pygame

class Character(Physics):
    def __init__(self, hp, position, sprite):
        super(Character, self).__init__(img_path=sprite, position = position)
        self.hp = hp
        self.rect = self.image.get_rect()
        # self.abajo, self.arriba, self.dcha, self.izq = self._cortar_chara(fil=3)
        self.movimientos = self._cortar_chara(fil=3)

    # Corta un chara en las fil y col indicadas.
    def _cortar_chara(self, fil):
        # La idea de esta función es devolver una tupla con cuatro vectores:
        #       * sprites de movimiento hacia la izquierda
        #       * sprites de movimiento hacia la derecha
        #       * sprites de movimiento hacia arriba
        #       * sprites de movimiento hacia abajo
        abajo = [0]*fil
        arriba = [0]*fil
        dcha = [0]*fil
        izq = [0]*fil

        for i in range(fil):
            abajo[i]  = (i*32, 0, 32, 32)
            izq[i]    = (i*32, 32, 32, 32)
            dcha[i]   = (i*32, 64, 32, 32)
            arriba[i] = (i*32, 96, 32, 32)

        return ({'A':abajo, 'U':arriba, 'D':dcha, 'I':izq})

    def draw(self, screen):
        screen.blit(self.image, self.position, self.movimientos[self.direction][self.index])

    def attack(self):
        raise NotImplemented("Implement the atack in MainCharacter and Enemy")

    def movement(self):
        raise NotImplemented("Implement the atack in MainCharacter and Enemy")

    def jump(self):
        if self.on_ground:
            self.change_y_speed_vector(-20)
            self.on_ground=False
        # self.rect.y += 2
        # platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        # self.rect.y -= 2
        # # If it is ok to jump, set our speed upwards
        #
        # if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
        #     self.__position_y__ = -10