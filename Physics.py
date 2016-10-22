import math, pygame
from graphics import load_image

"""Physics.py"""

"""Class that implement the physics of particles, such
    as characters, throwing weapons, etc."""

class Physics(pygame.sprite.Sprite):

    def __init__(self, img_path, x_position = 0., y_position = 0.):
        # position of particle (X, Y)
        self.__position_x__ = x_position
        self.__position_y__ = y_position
        # speed component of the particle
        self.__speed_vector__ = 0.
        # movement angle of vector
        self.__angle__ = 0.
        # Create an image of the block, and fill it with a image from disk.
        # self.image = pygame.Surface([self.__position_x__, self.__position_y__])
        self.image = load_image(img_path, transparent=False)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        # Depending on the window size, the particles will
        # have different limits
        # self.__limits__

        def collisions(self, group, destroy_ob):