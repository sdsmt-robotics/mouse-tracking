#!/usr/bin/python3
from robot import Robot
import os


def main():
    # disable mouse acceleration so the pointer follows the turtle
    os.system('xset m 00')

    jerry = Robot()
    jerry.track_motion()

    # reenable mouse acceleration when we're done
    os.system('xset m 11')


if __name__ == '__main__':
    main()
