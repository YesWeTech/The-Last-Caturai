#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""config.py"""

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

"""Config file for defining screen resolution (max available) and folder structure"""

# Import pygame
import pygame
from pygame.locals import *
import sys

# Nombre del juego
name = "The Last Caturai"

# Default screen resolution - window sizs
WIDTH = 800
HEIGHT = 600

# Folder structure
sprites = "resources/graphics/sprites/"
backs = "resources/graphics/backgrounds/"
menus = "resources/graphics/menus/"
music = "resources/audio/music/"
sounds = "resources/audio/sounds/"
fonts = "resources/fonts/"
levels = "levels/"
character_sprite = "prueba.png"
main_music = "Rosver_-_Atomic_Weight_8Bit.mp3"
jump_sound = "270323__littlerobotsoundfactory__jump-03.wav"
