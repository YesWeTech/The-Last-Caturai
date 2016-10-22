#! /usr/bin/env python
# -*- coding: utf-8 -*-

import Enemy

class Carp(Enemy):
    def __init__(self, hp, position, sprite):
        super(Carp, self).__init__(hp, position, sprite)

    def attack(self):
        pass
