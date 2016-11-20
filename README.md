# mouse-tracking
Use a USB mouse for tracking planar motion. The idea being that we can easily localize a robot using something that was literally designed for tracking 2D motion.

Run `sudo python3 mouse_data.py` to view almost raw data coming off the mouse.

Run `sudo python3 track_mouse.py` to view the mouse input using Turtle. A left click will reset the state.

You can read about how Linux handles mice [here](http://wiki.osdev.org/Mouse_Input#Mouse_Packet_Info).

You can turn mouse acceleration off (on Ubuntu at least) with `xset m 00` and back on again with `xset m 11`. Note that this won't affect the values read from `/dev/input/mice`, but it will affect where your OS displays your cursor with respect to the robot Turtle if you're testing with a GUI.

I've attempted to separate interfacing with the mouse and visualizing (and eventually computation) into two separate classes `Robot` and `Mouse` This isn't really necessary, but `Robot` inherits from `Turtle`, which has many of the things we need, so it works fairly well.

Note that I've mapped whatever units the mouse gives to millimeters by experimentally finding `71 mm / 2600 units`. This might change according to the surface we use.
