import math, pygame
from graphics import load_image

"""Physics.py"""

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

"""Class that implement the physics of particles, such
    as characters, throwing weapons, etc."""

class Physics(pygame.sprite.Sprite):

    def __init__(self, position = (0,0)):
        # position of particle (X, Y)
        self.__position__ = position
        # speed component of the particle
        self.__speed_vector__ = 0.
        # movement angle of vector
        self.__angle__ = 0.
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        # Depending on the window size, the particles will
        # have different limits
        # self.__limits__

        def collisions(self, group, destroy_ob):
            pass