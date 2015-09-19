#
# robot
# Josh Artuso
# September 18, 2015
#
# Just a basic robot object
#

import pygame


class Robot(pygame.sprite.Sprite):

    robot_width = 60
    robot_height = 80

    sprite_list = None
    game_display = None
    message_area = None

    sent_messages = []

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

    def configure(self, sprites, display, messages):
        """
        Configure the robot
        :return: None
        """
        self.sprite_list = sprites
        self.game_display = display
        self.message_area = messages

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

    def send_message(self, msg):
        """
        Send a message to the screen
        :param msg: The message to put on the screen
        :return: None
        """
        self.sent_messages.append(msg)
        self.preform_update()

    def clear_messages(self):
        """
        Clear all messages from the screen
        :return:
        """
        self.sent_messages = []
        self.preform_update()

    def preform_update(self):
        """
        Updates the display
        :return: None
        """
        self.game_display.fill((255, 255, 255))
        self.sprite_list.draw(self.game_display)
        for i in range(0, len(self.sent_messages)):
            screen_text = self.message_area.render(self.sent_messages[i], True, (0, 0, 255))
            self.game_display.blit(screen_text, [0, 15*i])
        pygame.display.update()
