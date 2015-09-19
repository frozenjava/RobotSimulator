#
# simulator
# Josh Artuso
# September 18, 2015
#
# The simulator
# Not working on OSX at the moment because OSX wont let you render the pygame window outside of the main thread.
# Fucking Apple....
#

import pygame
import threading


class Simulator(threading.Thread):

    # Vars
    ROBOT = None
    WIDTH = 800
    HEIGHT = 600
    COLORS = {"white": (255, 255, 255),
              "black": (0, 0, 0),
              "red": (255, 0, 0)
              }

    def __init__(self, robot, width=800, height=600):
        threading.Thread.__init__(self)
        self.ROBOT = robot
        self.WIDTH = width
        self.HEIGHT = height
        print "Initialized"

    def run(self):
        debug = 0

        print debug
        debug += 1

        # Initialize pygame
        pygame.init()

        print debug
        debug += 1

        # Create a surface object
        simulator_display = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        print debug
        debug += 1

        # Set the title of the window
        pygame.display.set_caption("jBot Simulator")

        # Create a pygame clock object
        clock = pygame.time.Clock()

        # Set the initial environment
        simulator_display.fill(self.COLORS.get("white"))
        self.ROBOT.configure_robot(self.WIDTH/2, self.HEIGHT/2, [self.WIDTH, self.HEIGHT])
        self.ROBOT.draw_robot(pygame, simulator_display)
        pygame.display.update()

        simulator_exit = False

        while not simulator_exit:
            print debug
            debug += 1

            # Handle each event
            for event in pygame.event.get():
                # Quit event
                if event.type == pygame.QUIT:
                    simulator_exit = True

            self.ROBOT.preform_update(pygame, simulator_display, self.COLORS.get("white"))
            clock.tick(20)

        pygame.quit()
        quit()
