#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""scene_game.py"""

"""Class SceneGame, the first scene of the game, when it starts."""

import scene
import pygame
import config
import graphics
from pygame.locals import *

class SceneGame(scene.Scene):

    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.back = graphics.load_image(config.backs+"temp_background.png", False)

    def on_update(self):
        pass

    def on_event(self):
        pass

    def on_draw(self, screen):
        infoScreen = pygame.display.Info()
        event = pygame.event.wait()
        if event.type == VIDEORESIZE:
            screen.blit(pygame.transform.scale(self.back, event.dict['size']), (0,0))
        else:
            screen.blit(pygame.transform.scale(self.back, (infoScreen.current_w, infoScreen.current_h)), (0,0))
