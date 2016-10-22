#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""main.py"""

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
