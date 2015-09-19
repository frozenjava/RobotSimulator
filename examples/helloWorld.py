from jbot import simulator


def print_a_message(msg):
    print msg


if __name__ == "__main__":
    simulator.simulate(print_a_message, "hello world")