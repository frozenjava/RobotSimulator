#
# simulator
# Josh Artuso
# September 18, 2015
#
# The simulator
#

import pygame

from multiprocessing import Process


def run_simulator(robot, width=800, height=600):
    p = Process(target=simulator, args=(robot, width, height))
    p.start()


def simulator(robot, width=800, height=600):
    
    colors = {"white": (255, 255, 255), "black": (0, 0, 0), "red": (255, 0, 0)}

    # Initialize pygame
    pygame.init()

    # Create a surface object
    simulator_display = pygame.display.set_mode((width, height))

    # Set the title of the window
    pygame.display.set_caption("jBot Simulator")

    # Create a pygame clock object
    clock = pygame.time.Clock()

    # Set the initial environment
    simulator_display.fill(colors.get("white"))
    robot.configure_robot(width / 2, height / 2, [width, height])
    robot.draw_robot(pygame, simulator_display)
    pygame.display.update()

    simulator_exit = False

    while not simulator_exit:

        # Handle each event
        for event in pygame.event.get():
            # Quit event
            if event.type == pygame.QUIT:
                simulator_exit = True

        robot.preform_update(pygame, simulator_display, colors.get("white"))
        clock.tick(20)

    pygame.quit()
    quit()
