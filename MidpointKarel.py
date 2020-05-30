from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    finding the midpoint for Karel
    """

    movement_condition()
    corner_condition()





def corner_condition():
    while front_is_blocked():
        turn_left()
        turn_left()
    if beepers_present():
        move()
    else:
        put_beeper()
        move()

def movement_condition():
    while front_is_clear():
        move()

















def about_turn():
    turn_left()
    turn_left()








# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
