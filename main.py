#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""main.py"""

"""Main file. Initialises pygame."""

import pygame, sys
from pygame.locals import *
import config

# Define main
def main():
    # Creating screen
    infoScreen = pygame.display.Info()
    screen = pygame.display.set_mode((infoScreen.current_w, infoScreen.current_h))
    pygame.display.set_caption(config.name)

    # Maintains screen opened unless manually closed
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
    return 0

# Initialise pygame
if __name__ == '__main__':
    pygame.init()
    main()
