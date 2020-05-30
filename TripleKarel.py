from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    """
    The following code tries to paint building by building. The first for loop is for the number of buildings and
    the next for loop is for the walls of the building.
    """

    for i in range(3):
        for j in range(2):
            building__painting()
            move_karel()
        building__painting()
        turn_right()


"""
This function paints the walls of a building 
"""
def building__painting():
    while left_is_blocked():
        put_beeper()
        move()

"""
This function moves karel to the next wall for painting
"""
def move_karel():
    turn_left()
    move()

"""
This turns Karel towards right
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program()
