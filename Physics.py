import math, pygame
from graphics import load_image

"""Physics.py"""

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