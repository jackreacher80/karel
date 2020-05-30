from karel.stanfordkarel import *


def main():
    # TODO write your solution here
    if beepers_present():
        draw_diagnol()
    else:
        put_beeper()
        draw_diagnol()



# There is no need to edit code beyond this point

def draw_diagnol():
    while front_is_clear():

        turn_left()
        move()
        turn_right()
        for i in range(2):

            if front_is_blocked():
                turn_right()
                turn_left()
            else:
                move()
        put_beeper()
    pick_beeper()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


if __name__ == "__main__":
    run_karel_program()