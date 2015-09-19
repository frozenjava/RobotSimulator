#
# robot
# Josh Artuso
# September 18, 2015
#
# Just a basic robot object
#

import os
import pygame


class Robot(pygame.sprite.Sprite):

    robot_width = 60
    robot_height = 80

    sprite_list = None
    game_display = None

    image = None
    rect = None

    def __init__(self, image=None, start_x=None, start_y=None, boundaries=None):
        # Call parent constructor
        pygame.sprite.Sprite.__init__(self)

        if image is None:
            self.image = pygame.Surface([self.robot_width, self.robot_height])
            self.image.fill((0, 255, 0))
            self.rect = self.image.get_rect()
        else:
            self.image = pygame.image.load(image).convert()
            self.rect = self.image.get_rect()

        if start_x is not None:
            self.rect.x = start_x

        if start_y is not None:
            self.rect.y = start_y

        if boundaries is not None:
            self.BOUNDARIES = boundaries

    def configure(self, sprites, display):
        """
        Configure the robot
        :return: None
        """
        self.sprite_list = sprites
        self.game_display = display

    def move_down(self, units):
        """
        Move the robot down the y axis
        :param units: The number of units to move
        :return: None
        """
        while units > 0:
            self.rect.y += 1
            units -= 1
            self.preform_update()

    def move_up(self, units):
        """
        Move the robot up the y axis
        :param units: The number of units to move
        :return: None
        """
        while units > 0:
            self.rect.y -= 1
            units -= 1
            self.preform_update()

    def move_left(self, units):
        """
        Move the robot left on the x axis
        :param units: The number of units to move
        :return: None
        """
        while units > 0:
            self.rect.x -= 1
            units -= 1
            self.preform_update()

    def move_right(self, units):
        """
        Move the robot down
        :param units: The number of units to move
        :return: None
        """
        while units > 0:
            self.rect.x += 1
            units -= 1
            self.preform_update()

    def preform_update(self):
        """
        Updates the display
        :return: None
        """
        self.game_display.fill((255, 255, 255))
        self.sprite_list.draw(self.game_display)
        pygame.display.update()
