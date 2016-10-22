#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""main.py"""

"""Main file. Initialises pygame."""

import pygame
import director
import scene_game

def main():
    dir = director.Director()
    scene = scene_game.SceneGame(dir)
    dir.change_scene(scene)
    dir.loop()

if __name__ == '__main__':
    pygame.init()
    main()
