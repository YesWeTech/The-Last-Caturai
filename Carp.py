#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""carp.py"""

"""The carp is the final enemy of the game."""

import Enemy

class Carp(Enemy):
    def __init__(self, hp, position, sprite):
        super(Carp, self).__init__(hp, position, sprite)

    def final_attack(self):
        pass

    def attack(self):
        pass

    def movement(self):
        pass
