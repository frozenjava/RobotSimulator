# jBot Simulator
This is a "robot simulator" for educational use.

I am a testing a hypothesis that students will learn programming concepts better if they see an object moving around on the screen, in this case a little robot looking guy.

Check out this video demonstration of the module

[![Click Here](http://i.imgur.com/S2lMpEU.png)](https://www.youtube.com/watch?v=laHVwjuu-24)

# Setup Instructions
### Windows & Linux
```
pip install pygame
python jbot/setup.py install
```

### Mac
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew update
brew install sdl sdl_image sdl_mixer sdl_ttf smpeg portmidi mercurial
brew install Caskroom/cask/xquartz
---- REBOOT YOUR MACHINE BEFORE CONTINUING ----
pip install hg+http://bitbucket.org/pygame/pygame
git clone https://github.com/frozenjava/RobotSimulator.git
python RobotSimulator/setup.py install
```

## Getting Started

You will need to import simulator into your python script to make use of all the functionality of jBot

```python
from jbot import simulator
```

In order to make the simulator run a simulation you need to call the simulate function from simulator.
This function takes two arguments:
```
    fun
        The user defined function to execute in the simulation
    *args
        Any arguments needed for the fun function
```     

### Hello World

Here is a quick sample program that will print hello world in the simulation

```python
from jbot import simulator


def print_a_message(msg):
    print msg


if __name__ == "__main__":
    simulator.simulate(print_a_message, "hello world")

```

You can have as many functions as you would like in your code. Just make the function being passed to simulate call the other functions.

### Controlling The Robot

To get the instance of the robot from the simulator you use the get_robot function in simulator.

```python
my_robot = simulator.get_robot()
```

This will return an instance of Robot.

Robot has the following messages:

```
    move_up(units)
        Moves the robot a specified number of units up
        
    move_down(units)
        Moves the robot a specified number of units down
        
    move_left(units)
        Moves the robot a specified number of units to the left
        
    move_right(units)
        Moves the robot a specified number of units to the right
        
    send_message(msg)
        Displays a message in the top left corner of the simulation
        
    clear_messages()
        Removes all messages from the top left corner of the simulation
```

Here is an example that will move the robot around in the simulation and send messages about what its doing.

```
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
```