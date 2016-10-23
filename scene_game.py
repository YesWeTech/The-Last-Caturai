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
from Enemy import Enemy
from Character import Character
import platform

class SceneGame(scene.Scene):

    platform_list = None
    enemy_list = None

    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000

    def __init__(self, director):
        scene.Scene.__init__(self, director)
        #self.back = graphics.load_image(config.backs+"temp_background.png", False)
        # pygame.mixer.music.load(os.path.abspath("resources/audio/music/Rosver_-_Atomic_Weight_8Bit.mp3"))
        # pygame.mixer.music.play(1)
        self.background = graphics.load_image(config.backs+"level1_background.png", False)
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.enemy_list.add(Enemy(hp=10, position=(400,config.HEIGHT - 100), sprite=os.path.abspath(config.sprites + config.character_sprite)))
        self.player = director.main_character

    def on_update(self):
        self.platform_list.update()
        self.enemy_list.update()

    def on_event(self, shift_x):
        self.world_shift += shift_x

        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

    def on_draw(self, screen, seconds, player):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(config.back_colour)
        screen.blit(self.background, (self.world_shift // 3,0))
        player.world_shift = self.world_shift
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

        infoScreen = pygame.display.Info()

        #Load timer
        timer_label, timer_label_rect = graphics.text("Time: ", infoScreen.current_w - 200, 30, config.font_colour,
                                          40)
        timer, timer_rect = graphics.text("{00000000}".format(seconds), infoScreen.current_w-80, 30, config.font_colour, 40)
        #screen.blit(pygame.transform.scale(self.back, (infoScreen.current_w, infoScreen.current_h)), (0,0))
        #screen.blit(timer, timer_rect)
        #screen.blit(timer_label, timer_label_rect)

        #Load main character
        player.draw(screen)

    def on_resize(self, screen, event):
        screen = pygame.display.set_mode(event.dict['size'], HWSURFACE|DOUBLEBUF|RESIZABLE)
        screen.blit(pygame.transform.scale(self.back, event.dict['size']), (0,0))

# Create platforms for the level
class Level_01(SceneGame):
    """ Definition for level 1. """

    def __init__(self, director):
        """ Create level 1. """

        # Call the parent constructor
        SceneGame.__init__(self, director)

        self.background = graphics.load_image(config.backs+"temp_background.png", False)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS_UP, 500, 500],
                  [platforms.GRASS_DOWN, 570, 500],
                  [platforms.GRASS_UP, 640, 500],
                  [platforms.GRASS_DOWN, 800, 400],
                  [platforms.GRASS_DOWN, 870, 400],
                  [platforms.GRASS_DOWN, 940, 400],
                  [platforms.STONE_PLATFORM_UP, 1120, 280],
                  [platforms.STONE_PLATFORM_DOWN, 1190, 280],
                  [platforms.STONE_PLATFORM_DOWN, 1260, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_UP)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        # block.level = self
        self.platform_list.add(block)
