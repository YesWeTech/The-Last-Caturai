import math, pygame
from graphics import load_image
import constants

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

        # speed component of the particle
        self.__x_speed_vector__ = 0.
        # movement angle of vector
        self.__y_speed_vector__ = 0.
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    # Set the value of the speed vector
    def change_x_speed_vector(self, speed):
        self.__x_speed_vector_ = abs(speed)

    # Set the angle of the movement in radians
    def change_y_speed_vector(self, angle):
        self.__y_speed_vector__ = abs(angle)

    def move_right(self):
        self.__position_x__ += self.__x_speed_vector__

    def move_left(self):
        self.__position_x__ -= self.__x_speed_vector__

    def stop_moving(self):
        self.change_x_speed_vector(0)
        self.change_y_speed_vector(0)

    def go_up(self):
        self.__y_speed_vector__ -= self.__y_speed_vector__

    def go_down(self):
        self.__y_speed_vector__ += self.__y_speed_vector__

    def gravity(self):
        """ Calculate effect of gravity. """
        if self.__position_y__ == 0:
            self.__position_y__ = 1
        else:
            self.__position_y__ += .35

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.__position_y__ >= 0:
            self.__position_y__ = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

