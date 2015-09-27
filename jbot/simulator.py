import pygame
import sys
import os
from threading import Thread

from jbot.robot import Robot
from jbot.wall import Wall

jBot = None


def get_robot():
    return jBot


def send_simulator_message(msg, msg_area, display, location):
    screen_text = msg_area.render(msg, True, (255, 0, 0))
    display.blit(screen_text, location)


def simulate(fun, *args):

    global jBot

    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)
    images_path = dir_path + "/images/"
    width = 800
    height = 600

    colors = {"white": (255, 255, 255),
              "black": (0, 0, 0),
              "red": (255, 0, 0),
              "green": (0, 255, 0),
              "blue": (0, 0, 255),
              "pink": (255, 200, 200)}

    pygame.init()  # Create a surface object
    simulator_display = pygame.display.set_mode((width, height))

    # Set the title of the window
    pygame.display.set_caption("jBot Simulator")

    # Texts
    robo_messages = pygame.font.SysFont(None, 25)
    sim_messages = pygame.font.SysFont(None, 25)

    # A list of all sprites
    all_sprites_list = pygame.sprite.Group()
    wall_sprites = pygame.sprite.Group()

    # The robot
    jBot = Robot(image=images_path + "jbot.png", start_x=0, start_y=height-80)
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

    # Create a pygame clock object
    clock = pygame.time.Clock()

    # Set the initial environment
    simulator_display.fill(colors.get("white"))
    jBot.configure(all_sprites_list, simulator_display, robo_messages)
    all_sprites_list.draw(simulator_display)

    send_simulator_message("Press any key to start simulation", sim_messages, simulator_display,
                           [(width/2), height/2])
    pygame.display.update()

    simulator_exit = False
    t = None

    while not simulator_exit:

        pygame.sprite.spritecollide(jBot, wall_sprites, False)

        # Handle each event
        for event in pygame.event.get():
            # Quit event
            if event.type == pygame.QUIT:
                simulator_exit = True
            elif event.type == pygame.KEYDOWN:
                simulator_display.fill(colors.get("white"))
                pygame.display.update()
                t = Thread(target=fun, args=args)
                t.start()

        if t is not None:
            if not t.isAlive():
                simulator_exit = True

        clock.tick(20)

    exit_simulator = False
    while not exit_simulator:

        send_simulator_message("Press q to quit simulation", sim_messages, simulator_display,
                               [(width/2)-len("Press q to quit simulation"), (height/2)])
        pygame.display.update()

        # Handle each event
        for event in pygame.event.get():
                # Quit event
                if event.type == pygame.QUIT:
                    exit_simulator = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        exit_simulator = True

    pygame.quit()
    sys.exit()
