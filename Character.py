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

class Character(Physics):
    def __init__(self, hp, position, sprite):
        super(Character, self).__init__(img_path=sprite, position = position)
        self.hp = hp
        self.rect = self.image.get_rect()
        self.abajo, self.arriba, self.dcha, self.izq = self._cortar_chara(fil=3)

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
            abajo[i]  = (0,  i*32, 32, 32)
            izq[i]    = (32, i*32, 32, 32)
            dcha[i]   = (64, i*32, 32, 32)
            arriba[i] = (96, i*32, 32, 32)

        return (abajo, arriba, dcha, izq)

    def draw(self, screen):
        screen.blit(self.image, self.position, self.abajo[0])

    def attack(self):
        raise NotImplemented("Implement the atack in MainCharacter and Enemy")

    def movement(self):
        raise NotImplemented("Implement the atack in MainCharacter and Enemy")
