#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""scene_game.py"""

"""Class SceneGame, the first scene of the game, when it starts."""

import scene
import config
import graphics

class SceneGame(scene.Scene):

    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.back = graphics.load_image(config.backs+"temp_background.png", False)

    def on_update(self):
        pass

    def on_event(self):
        pass

    def on_draw(self, screen):
        screen.blit(self.back, (0,0))
