#! /usr/bin/env python
# -*- coding: utf-8 -*-

import Character

class Enemy(Character):
    def __init__(self, hp, position, sprite):
        super(Enemy, self).__init__(hp, position, sprite)
        
