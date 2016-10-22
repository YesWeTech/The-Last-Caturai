#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""character.py"""

"""Defines an abstract character"""

from graphics import load_image

class Character:
    def __init__(self, hp, position, sprite):
        self.hp = hp
        self.position = position
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
