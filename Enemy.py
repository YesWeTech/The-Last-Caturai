#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""enemy.py"""

"""It defines the general enemies of the game."""

import Character

class Enemy(Character):
    def __init__(self, hp, position, sprite):
        super(Enemy, self).__init__(hp, position, sprite)

    def attack(self):
        pass

    def movement(self):
        pass
