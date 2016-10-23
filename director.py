#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""director.py"""

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

"""Class Director, it contains the game loop, and manages events."""

import pygame
import os
import config
from MainCharacter import MainCharacter
import graphics
from pygame.locals import *
import scene_game

class Director:

    def __init__(self):
        infoScreen = pygame.display.Info()
        self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        pygame.display.set_caption(config.name)
        self.scene = None
        self.quit_flag = False
        self.clock = pygame.time.Clock()
        self.main_character = MainCharacter(hp=100, position=(100,config.GROUND_HEIGHT), sprite=os.path.abspath(config.sprites + config.character_sprite),is_girl=True)
        #self.CreateHealthBar(self.main_character.hp, self.screen)

    def CreateHealthBar(self, health, screen):
        if health > 75:
            character_health_color = (  0, 255,   0) #GREEN
        elif health > 50:
            character_health_color = (255, 255,   0) #YELLOW
        else:
            character_health_color = (255,   0,   0) #RED

        pygame.draw.rect(screen, character_health_color, (45, 10, health, 25))
        pygame.display.update()

    def loop(self):
        """Starts the game"""

        seconds = 0
        index = 0

        while not self.quit_flag:
            self.time = self.clock.tick(60)
            # Exit events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or pygame.key.get_pressed()[pygame.K_LEFT]:
                        self.main_character.move_left()

                    if event.key == pygame.K_RIGHT or pygame.key.get_pressed()[pygame.K_RIGHT]:
                        self.main_character.move_right()

                    if event.key == pygame.K_UP:
                        if self.main_character.on_ground:
                            jump_sound = pygame.mixer.Sound(
                                os.path.abspath(config.sounds+config.jump_sound))
                            jump_sound.play()
                            self.main_character.jump()

                    if event.key == pygame.K_RCTRL:
                        self.main_character.attack(self.scene.enemy_list)



                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and self.main_character.x_speed_vector_ < 0:
                        self.main_character.stop_moving()
                    if event.key == pygame.K_RIGHT and self.main_character.x_speed_vector_ > 0:
                        self.main_character.stop_moving()

            self.main_character.update()


            # Scene update
            self.scene.on_update()
            pygame.display.update()

            # Event detection
            #self.scene.on_event()

            # If the player gets near the right side, shift the world left (-x)
            if self.main_character.rect.x >= 500:
                diff = self.main_character.rect.x - 500
                self.main_character.rect.x = 500
                self.scene.on_event(-diff)

            # If the player gets near the left side, shift the world right (+x)
            if self.main_character.rect.x <= 120:
                diff = 120 - self.main_character.rect.x
                self.main_character.rect.x = 120
                self.scene.on_event(diff)

                # Draws scene
            seconds += self.time

            if self.main_character.hp <= 0:
                self.scene.on_draw(self.screen, seconds, False)
            elif self.main_character.rect.x >= 2790:
                self.scene.on_draw(self.screen, seconds, True)
            else:
                self.scene.on_draw(self.screen, seconds, self.main_character)

            if self.main_character.hp > 0:
                timer_label, timer_label_rect = graphics.text("HP ", 30, 20, config.font_colour,40)
                self.screen.blit(timer_label, timer_label_rect)
                self.CreateHealthBar(self.main_character.hp, self.screen)

            pygame.display.flip()

    def change_scene(self, scene):
        """Updates actual scene"""
        self.scene = scene

    def quit(self):
        self.quit_flag = True
