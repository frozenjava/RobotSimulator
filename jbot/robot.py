#
# robot
# Josh Artuso
# September 18, 2015
#
# Just a basic robot object
#


class Robot(object):

    COORD_X = 0
    COORD_Y = 0

    COORD_X_CHANGE = 0
    COORD_Y_CHANGE = 0

    COLOR = (255, 0, 0)
    ROBOT_HEIGHT = 10
    ROBOT_WIDTH = 10

    BOUNDARIES = []

    VISUAL_UPDATE_NEEDED = False

    def __init__(self, start_x=None, start_y=None, boundaries=None):
        if start_x is not None:
            self.COORD_X = start_x

        if start_y is not None:
            self.COORD_Y = start_y

        if boundaries is not None:
            self.BOUNDARIES = boundaries

    def configure_robot(self, coord_x, coord_y, boundaries):
        """
        This method will just configure the robot in the simulator
        :param coord_x:
        :param coord_y:
        :return:
        """
        self.COORD_X = coord_x
        self.COORD_Y = coord_y
        self.BOUNDARIES = boundaries

    def draw_robot(self, py_game, simulator_display):
        """
        Draw the robot on the screen
        :param py_game: Pygame instance
        :param simulator_display: pygame display instance
        :return: None
        """
        py_game.draw.rect(simulator_display, self.COLOR, [self.COORD_X, self.COORD_Y,
                                                          self.ROBOT_WIDTH, self.ROBOT_HEIGHT])
        
    def request_update_x(self, value):
        """
        Update the ROBOTs x position
        :param value: The value to change x by
        :return:
        """
        if not self.check_x_boundary(value):
            self.COORD_X_CHANGE = value
        else:
            if self.correct_x_position(value) >= 0:
                self.COORD_X_CHANGE = self.correct_x_position(value)

    def request_update_y(self, value):
        """
        Update the ROBOTs y position
        :param value: The value to change y by
        :return:
        """
        if not self.check_y_boundary(value):
            self.COORD_Y_CHANGE = value
        else:
            if self.correct_y_position(value) >= 0:
                self.COORD_Y_CHANGE = self.correct_y_position(value)

    def check_x_boundary(self, value=0):
        """
        Check if the ROBOT is at the boundaries of the game
        :param value: The value pixels that the ROBOT will move next
        :return:
        """
        move_distance = self.ROBOT_WIDTH / 2
        if self.COORD_X + value >= self.BOUNDARIES[0] - move_distance or self.COORD_X + value < 0:
            return True
        else:
            return False

    def check_y_boundary(self, value=0):
        """
        Check if the ROBOT is at the boundaries of the game
        :param value: The value pixels that the ROBOT will move next
        :return:
        """
        move_distance = self.ROBOT_WIDTH / 2
        if self.COORD_Y + value >= self.BOUNDARIES[1] - move_distance or self.COORD_Y + value < 0:
            return True
        else:
            return False

    def correct_x_position(self, value=0):
        """
        Correct the ROBOTs x axis position if the pass the boundary
        :return:
        """
        if self.COORD_X + value > self.BOUNDARIES[0] - self.ROBOT_WIDTH:
            return (self.COORD_X + value) - (self.BOUNDARIES[0] - self.ROBOT_WIDTH)
        elif self.COORD_X + value < 0 < self.COORD_X:
            return (self.COORD_X + value) + self.ROBOT_WIDTH

        return 0

    def correct_y_position(self, value=0):
        """
        Correct the ROBOTs y axis position if the pass the boundary
        :return:
        """
        if self.COORD_Y + value > self.BOUNDARIES[1] - self.ROBOT_HEIGHT:
            return (self.COORD_Y + value) - (self.BOUNDARIES[0] - self.ROBOT_HEIGHT)
        elif self.COORD_Y + value < 0 < self.COORD_Y:
            return (self.COORD_Y + value) + self.ROBOT_HEIGHT

        return 0

    def update_position(self):
        """
        Change the ROBOTs position
        :return:
        """
        # Check if the ROBOT has hit the boundary
        if self.check_x_boundary(self.COORD_X_CHANGE):
            self.COORD_X_CHANGE = 0

        if self.check_y_boundary(self.COORD_Y_CHANGE):
            self.COORD_Y_CHANGE = 0

        self.COORD_X += self.COORD_X_CHANGE
        self.COORD_Y += self.COORD_Y_CHANGE

        if self.COORD_X_CHANGE is not 0 or self.COORD_Y_CHANGE is not 0:
            return True
        else:
            return False
        
    def preform_update(self, py_game, game_display, color):
        """
        Update the robot on the screen
        :param py_game: the pygame module
        :param game_display: pygame display instance
        :param color: the background color
        :return:
        """
        updated_needed = self.update_position()

        if updated_needed or self.VISUAL_UPDATE_NEEDED:
            game_display.fill(color)
            self.draw_robot(py_game, game_display)
            py_game.display_update()
            self.VISUAL_UPDATE_NEEDED = False
