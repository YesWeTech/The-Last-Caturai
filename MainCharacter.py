#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""MainCharacter.py"""

"""Defines the main character of the game"""

import Character

class MainCharacter(Character):
    def __init__(self, hp, position, sprite, is_girl):
        super(MainCharacter, self).__init__(hp, position, sprite)
        self.is_girl = is_girl

    def attack(self):
        pass

    def movement(self):
        pass    
