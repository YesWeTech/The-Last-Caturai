#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""scene_game.py"""

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

"""Class SceneGame, the first scene of the game, when it starts."""

import scene
import pygame
import config
import graphics
import os
from pygame.locals import *

class SceneGame(scene.Scene):

    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.back = graphics.load_image(config.backs+"temp_background.png", False)

    def on_update(self):
        pass

    def on_event(self):
        pass

    def on_draw(self, screen, seconds):
        infoScreen = pygame.display.Info()
        font_color = (0, 0, 0)
        timer_label, timer_label_rect = graphics.text("Time: ", infoScreen.current_w - 200, 30, font_color,
                                          40)
        timer, timer_rect = graphics.text("{00000000}".format(seconds), infoScreen.current_w-80, 30, font_color, 40)
        screen.blit(pygame.transform.scale(self.back, (infoScreen.current_w, infoScreen.current_h)), (0,0))
        screen.blit(timer, timer_rect)
        screen.blit(timer_label, timer_label_rect)

        #sprite = graphics.get_image(os.path.abspath("resources/graphics/sprites/prueba.png"),100,100,2000,2000)
        image = graphics.load_image(os.path.abspath("resources/graphics/sprites/prueba.png"), True)
        screen.blit(image, (100,100))

    def on_resize(self, screen, event):
        screen = pygame.display.set_mode(event.dict['size'], HWSURFACE|DOUBLEBUF|RESIZABLE)
        screen.blit(pygame.transform.scale(self.back, event.dict['size']), (0,0))
