#!/usr/bin/python3
from mouse import Mouse


def read_mouse(filename='/dev/input/mice'):
    # http://wiki.osdev.org/Mouse_Input#Mouse_Packet_Info
    with Mouse() as mouse:
        while True:
            try:
                status, dx, dy = mouse.update()
                print('status: {}, dx: {}, dy: {}'.format(status, dx, dy))
            except KeyboardInterrupt:
                break


if __name__ == '__main__':
    read_mouse()
