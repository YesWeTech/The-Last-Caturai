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
import random
import platforms

class SceneGame(scene.Scene):

    platform_list = None
    enemy_list = None

    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000

    # distance when the enemy will start attacking
    enemy_distance = 250

    def __init__(self, director):
        scene.Scene.__init__(self, director)
        #self.back = graphics.load_image(config.backs+"temp_background.png", False)
        # pygame.mixer.music.load(os.path.abspath("resources/audio/music/Rosver_-_Atomic_Weight_8Bit.mp3"))
        # pygame.mixer.music.play(1)
        self.background = graphics.load_image(config.backs+"level1_shorter_background.png", False)
        self.game_over = graphics.load_image(config.backs+"game_over.png", False)
        self.you_win = graphics.load_image(config.backs + "you_win.png", False)
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        for i in range(5):
            self.enemy_list.add(Enemy(hp=10, position=(random.randrange(400,2000),config.GROUND_HEIGHT),
                                      sprite=os.path.abspath(config.sprites + config.character_sprite)))
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
            aux = list(enemy.shuriken.position)
            aux[0] += shift_x
            enemy.shuriken.position = aux

    def on_draw(self, screen, seconds, player):
        """ Draw everything on this level. """
        if player == False:
            screen.fill(config.back_colour)
            screen.blit(self.game_over, (self.world_shift // 3, 0))

        elif player == True:
            screen.fill(config.back_colour)
            screen.blit(self.you_win, (self.world_shift // 3, 0))
        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        else:
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
            for i in self.enemy_list.sprites():
                if abs(player.position[0] - i.position[0]) < self.enemy_distance or i.attacking:
                    i.attack(player=player, screen=screen)

            if player.hp >  0 :
                player.draw(screen)

    def on_resize(self, screen, event):
        screen = pygame.display.set_mode(event.dict['size'], HWSURFACE|DOUBLEBUF|RESIZABLE)
        screen.blit(pygame.transform.scale(self.back, event.dict['size']), (0,0))

# Create platforms for the level
class Level_01(SceneGame):

    def __init__(self, director):

        # Call the parent constructor
        SceneGame.__init__(self, director)

        self.background = graphics.load_image(config.backs+"level1_shorter_background.png", False)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.STONE_PLATFORM_LEFT, 700, 500],
                  [platforms.STONE_PLATFORM_MIDDLE, 770, 500],
                  [platforms.STONE_PLATFORM_RIGHT, 840, 500],
                  [platforms.STONE_PLATFORM_LEFT, 1000, 400],
                  [platforms.STONE_PLATFORM_MIDDLE, 1070, 400],
                  [platforms.STONE_PLATFORM_RIGHT, 1140, 400],
                  [platforms.STONE_PLATFORM_LEFT, 1200, 500],
                  [platforms.STONE_PLATFORM_MIDDLE, 1270, 500],
                  [platforms.STONE_PLATFORM_RIGHT, 1340, 500],
                  [platforms.STONE_PLATFORM_LEFT, 1320, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1390, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1460, 280],
                  [platforms.STONE_PLATFORM_LEFT, 1880, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1950, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 2020, 280],
                  [platforms.STONE_PLATFORM_LEFT, 2090, 500],
                  [platforms.STONE_PLATFORM_MIDDLE, 2160, 500],
                  [platforms.STONE_PLATFORM_RIGHT, 2230, 500],
                  [platforms.EXIT, 2510, 497],
                  [platforms.STONE_BLOCK, 2580, 497],
                  [platforms.STONE_BLOCK, 2650, 497],
                  [platforms.STONE_BLOCK, 2720, 497],
                  [platforms.DOOR, 2790, 497],
                  [platforms.STONE_BLOCK, 2860, 497],
                  [platforms.STONE_BLOCK, 2930, 497],
                  [platforms.STONE_BLOCK, 3000, 497],
                  [platforms.STONE_BLOCK, 2580, 427],
                  [platforms.STONE_BLOCK, 2650, 427],
                  [platforms.STONE_BLOCK, 2720, 427],
                  [platforms.STONE_BLOCK, 2790, 427],
                  [platforms.STONE_BLOCK, 2860, 427],
                  [platforms.STONE_BLOCK, 2930, 427],
                  [platforms.STONE_BLOCK, 3000, 427],
                  [platforms.STONE_BLOCK, 2580, 357],
                  [platforms.STONE_BLOCK, 2650, 357],
                  [platforms.STONE_BLOCK, 2720, 357],
                  [platforms.STONE_BLOCK, 2790, 357],
                  [platforms.STONE_BLOCK, 2860, 357],
                  [platforms.STONE_BLOCK, 2930, 357],
                  [platforms.STONE_BLOCK, 3000, 357],
                  [platforms.STONE_PLATFORM_MIDDLE, 2580, 317],
                  [platforms.STONE_PLATFORM_MIDDLE, 2720, 317],
                  [platforms.STONE_PLATFORM_MIDDLE, 2860, 317],
                  [platforms.STONE_PLATFORM_MIDDLE, 3000, 317],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1550
        block.rect.y = 280
        block.boundary_left = 1550
        block.boundary_right = 1800
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
