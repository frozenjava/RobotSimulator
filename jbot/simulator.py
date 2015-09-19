import pygame
import sys
import os

from jbot.robot import Robot
from jbot.wall import Wall

jBot = None


def get_robot():
    return jBot


def simulate(fun, *args):

    global jBot

    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)
    images_path = dir_path + "/images/"
    width = 800
    height = 600

    pygame.init()  # Create a surface object
    simulator_display = pygame.display.set_mode((width, height))

    colors = {"white": (255, 255, 255),
              "black": (0, 0, 0),
              "red": (255, 0, 0),
              "green": (0, 255, 0),
              "blue": (0, 0, 255),
              "pink": (255, 200, 200)}

    # A list of all sprites
    all_sprites_list = pygame.sprite.Group()
    wall_sprites = pygame.sprite.Group()

    # The robot
    jBot = Robot(image=images_path + "jbot.png", start_x=width / 2, start_y=height / 2)
    all_sprites_list.add(jBot)

    # The walls around the game
    left_wall = Wall(colors.get("pink"), 10, height, 0, 0)
    top_wall = Wall(colors.get("pink"), width, 10, 0, 0)
    right_wall = Wall(colors.get("pink"), 10, height, width-10, 0)
    bottom_wall = Wall(colors.get("pink"), width, 10, 0, height-10)
    wall_sprites.add(top_wall)
    wall_sprites.add(left_wall)
    wall_sprites.add(right_wall)
    wall_sprites.add(bottom_wall)
    all_sprites_list.add(left_wall)
    all_sprites_list.add(top_wall)
    all_sprites_list.add(right_wall)
    all_sprites_list.add(bottom_wall)

    # Set the title of the window
    pygame.display.set_caption("jBot Simulator")

    # Create a pygame clock object
    clock = pygame.time.Clock()

    # Set the initial environment
    simulator_display.fill(colors.get("white"))
    all_sprites_list.draw(simulator_display)
    pygame.display.update()

    simulator_exit = False

    jBot.configure(all_sprites_list, simulator_display)

    while not simulator_exit:

        pygame.sprite.spritecollide(jBot, wall_sprites, False)

        # Handle each event
        for event in pygame.event.get():
            # Quit event
            if event.type == pygame.QUIT:
                simulator_exit = True

        fun(*args)
        simulator_exit = True

        clock.tick(20)

    while raw_input("Press enter to continue"):
        pass


    pygame.quit()
    sys.exit()
