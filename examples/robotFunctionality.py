from jbot import simulator


def diagonal_moving(robot):
    robot.clear_messages()
    robot.send_message("moving diagonally")

    for m in range(0, 100):
        robot.move_left(1)
        robot.move_up(1)


def directional_moving(robot):

    robot.send_message("moving down")
    robot.move_down(30)

    robot.send_message("moving up")
    robot.move_up(60)

    robot.send_message("moving left")
    robot.move_left(25)

    robot.send_message("moving right")
    robot.move_right(600)


def main():
    my_robot = simulator.get_robot()
    directional_moving(my_robot)
    diagonal_moving(my_robot)
    my_robot.send_message("All Done!")

if __name__ == "__main__":
    simulator.simulate(main)

