#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""director.py"""

"""Class Director, it contains the game loop, and manages events."""

import pygame
import config
from pygame.locals import *

class Director:

    def __init__(self):
        infoScreen = pygame.display.Info()
        self.screen = pygame.display.set_mode((infoScreen.current_w, infoScreen.current_h), RESIZABLE)
        pygame.display.set_caption(config.name)
        self.scene = None
        self.quit_flag = False
        self.clock = pygame.time.Clock()

    def loop(self):
        """Starts the game"""

        while not self.quit_flag:
            self.time = self.clock.tick(60)

            # Exit events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

            # Event detection
            self.scene.on_event()

            # Scene update
            self.scene.on_update()

            # Draws scene
            self.scene.on_draw(self.screen)
            pygame.display.flip()

    def change_scene(self, scene):
        """Updates actual scene"""
        self.scene = scene

    def quit(self):
        self.quit_flag = True
