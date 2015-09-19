from jbot import simulator


def test_moving():
    raw_input("Press enter to run")
    robot = simulator.get_robot()
    print "moving down"
    robot.move_down(30)

    print "moving up"
    robot.move_up(60)

    print "moving left"
    robot.move_left(25)

    print "moving right"
    robot.move_right(600)


simulator.simulate(test_moving)

