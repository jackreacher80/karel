from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
This program solves the problem for StoneMasonKarel.py
"""


def main():
    """The main function calls function build_column(), jump_col_to_col"""

    """pre-condition- front is clear
       post-condition- front is not clear and loop terminates  
    """
    while front_is_clear():

        turn_left()
        build_column()
        while front_is_clear():
            move()
        turn_left()
        jump_col_to_col()

    """pre-condition- front is blocked
       post-condition- front is  clear and if terminates  
    """
    if front_is_blocked():
        turn_left()
        """pre-condition- front is clear
           post-condition- front is not clear and loop terminates  
        """
        while front_is_clear():
            """pre-condition- front is blocked
               post-condition- front is  clear and  terminates  
            """
            if beepers_present():
                move()
            else:
                put_beeper()
                move()
        """pre-condition- beeper is present at the last level
           post-condition- else put beeper
        """
        if beepers_present():
            turn_right()
            turn_left()
        else:
            put_beeper()





"""
This turns Karel two lefts which is 180 degrees
"""
def about_turn():
    turn_left()
    turn_left()

""" 
This builds a column
"""
def build_column():
    while front_is_clear():
        if beepers_present():
            move()
        else:
            put_beeper()
            move()

    if front_is_blocked():
        about_turn()
    if front_is_blocked():
        if beepers_present():
            for i in range(4):
                turn_left()
        else:
            put_beeper()
            for i in range(4):
                turn_left()

    while front_is_clear():
            # turn_left()
        if beepers_present():
            move()

        else:
            put_beeper()
            move()

"""
This turns Karel towards right
"""
def turn_right():
    for i in range(3):
        turn_left()

"""
This makes Karel move four blocks away toward the new wall
"""
def jump_col_to_col():
    for i in range(4):
        move()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()