import turtle
from mouse import Mouse

MM_PER_P = 71 / 2600  # experimentally determined average of values with lots of deviation


class Robot(turtle.Turtle):
	"""Robot inherits from Turtle, so we can make it work with mice and
	things."""
	def __init__(self):
		# call super to initialize a Robot as a Turtle
		super(Robot, self).__init__()
		self.start_x, self.start_y = self.position()
		self.screen = turtle.Screen()
		# only draw every 5 updates with a delay of 16 milliseconds (100 hz)
		self.screen.tracer(5, 10)

	def track_motion(self):
		"""starts tracking the motion of a mouse. (moution?)"""
		with Mouse() as mouse:
			while True:
				try:
					self.update(mouse)
				except:
					break

	def update(self, mouse):
		"""perform a single update to the Robot's position"""
		status, dx, dy = mouse.update()
		# left mouse click resets the robot position and heading
		if status[-1]:
			self.reset()
			self.start_x, self.start_y = self.position()

		x, y = self.position()

		x += dx
		y += dy
		self.setposition(x, y)
		radius = self.distance(self.start_x, self.start_y) * MM_PER_P

		print('x: {} y: {}'.format(x * MM_PER_P, y * MM_PER_P))
		print('\tdistance from the origin: {:.2f} mm'.format(radius))
