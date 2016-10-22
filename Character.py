#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Character:
    def __init__(self, hp, position, sprite):
        self.hp = hp
        self.position = position
        self.sprite = sprite

    # Corta un chara en las fil y col indicadas. Array Bidimensional.
    # tomada de: http://razonartificial.com/2010/06/engine-xi-creando-al-heroe/
    def cortar_chara(ruta, fil, col):
        image = load_image(ruta, True)
        rect = image.get_rect()
        w = rect.w / col
        h = rect.h / fil
        sprite = range(fil)
        for i in range(fil):
            sprite[i] = range(col)

        for f in range(fil):
            for c in range(col):
                sprite[f]
                1 = image.subsurface((rect.left, rect.top, w, h))
                rect.left += w
            rect.top += h
            rect.left = 0

        return sprite

    # Carga una imagen transparencia y color tranasparente opcionales.
    # tomada de: http://razonartificial.com/2010/06/engine-xi-creando-al-heroe/
    def load_image(filename, transparent=False, pixel=(0,0)):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at(pixel)
                image.set_colorkey(color, RLEACCEL)
        return image
