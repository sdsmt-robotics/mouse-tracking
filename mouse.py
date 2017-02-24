class Mouse(object):
    """Provides the ability to use `with Mouse() as mouse:` syntax to grab
    mouse updates over in the Robot class"""
    def __init__(self, filename='/dev/input/mice'):
        self.mouse = open(filename, 'rb')

    # __enter__ and __exit__ enable the with Mouse() as mouse: syntax
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.mouse.close()

    def update(self):
        """grab a single 3 byte update from the mouse `/dev/input/` file"""
        status, dx, dy = tuple(self.mouse.read(3))
        return self.interpret_status(status), self.to_signed(dx), self.to_signed(dy)

    def to_signed(self, num):
        # necessary for some reason in Python, but not C++
        return num - ((0x80 & num) << 1)

    def interpret_status(self, status):
        # http://wiki.osdev.org/Mouse_Input#Mouse_Packet_Info
        y_overflow = status & 0x80 > 0
        x_overflow = status & 0x40 > 0
        y_sign = status & 0x20 > 0
        x_sign = status & 0x10 > 0
        middle_button = status & 0x4 > 0
        right_button = status & 0x2 > 0
        left_button = status & 0x1 > 0

        return y_overflow, x_overflow, y_sign, x_sign, middle_button, right_button, left_button
