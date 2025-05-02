"""
File: Steeplechase.py
Name: Yi-Han
---------------------------------
TODO:
"""
from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()


def jump():
    """
    Pre-condition:Karel is on the left side of the wall,facing East
    Post-condition:Karel is on the right side of the wall
    """
    UP()
    cross()
    down()


def UP():
    """
    Pre-condition:Karel is on the left side of the wall,facing East
    Post-condition:Karel is at the upper left side of the wall
    """
    turn_left()
    while not right_is_clear():
        move()


def cross():
    """
    Pre-condition:Karel is on the upper left side of the wall,facing North
    Post-condition:Karel is on the upper right,facing South
    """
    turn_right()
    move()
    turn_right()


def down():
    """
    Pre-condition:Karel is on the upper right,facing South
    Post-condition:Karel is on the right side of the wall
    """
    while front_is_clear():
        move()


def turn_right():
    for i in range(3):
        turn_left()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
