"""
File: PotholeFilling.py
Name: Yi_Han
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    TODO:
    """
    pass
    for i in range(3):
        go_in()
        put_99()
        go_out()

def put_99():
    """
    repeat put beeper 99 times
    """
    for i in range(99):
        put_beeper()

def turn_right():
    """
    turn left three times equal to turn right
    """
    for i in range(3):
        turn_left()

def go_in():
    """
    pre-condition:karel is at the upper,left of the pothole,facing East
    .post-condition:Karel is in the pothole,facing South
    """
    move()
    turn_right()
    move()

def go_out():
    """
    pre-condition:karel is in the pothole,facing South
    .post-condition:Karel is at the upper,left of the pothole,facing East
    """
    for i in range(2):
        turn_left()
    move()
    turn_right()
    move()

# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
