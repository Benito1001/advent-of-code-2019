from intcomputer import IntcodeComputer

intcode = list(eval(open("data.dat", "r").readline()))

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def tupleify(self):
		return (self.x, self.y)

class PaintBot:
	def __init__(self, pos, dir):
		self.pos = pos
		self.dir = dir
		self.max_up = -float("inf")
		self.max_down = float("inf")
		self.max_right = -float("inf")
		self.max_left = float("inf")

	def rotate(self, dir):
		if dir == 0:
			self.dir += 90
		else:
			self.dir -= 90
		self.dir = self.dir % 360

	def move(self):
		# left or right
		if self.dir % 180 == 0:
			self.pos.x += 1 if self.dir == 0 else -1
		# opp or down
		else:
			self.pos.y += 1 if self.dir == 90 else -1
		self.max_up = max(self.max_up, self.pos.y)
		self.max_down = min(self.max_down, self.pos.y)
		self.max_right = max(self.max_right, self.pos.x)
		self.max_left = min(self.max_left, self.pos.x)


grid = {(0, 0): 1}
paint_bot = PaintBot(Point(0, 0), 90)

def input_func():
	return grid.get(paint_bot.pos.tupleify(), 0)

output = []
def output_func(val):
	global output
	output.append(val)
	if len(output) == 2:
		grid[paint_bot.pos.tupleify()] = output[0]
		paint_bot.rotate(output[1])
		paint_bot.move()
		output = []

computer = IntcodeComputer(intcode, input_func, output_func)
computer.run()

for y in range(paint_bot.max_up+2, paint_bot.max_down-2, -1):
	line = ""
	for x in range(paint_bot.max_left-2, paint_bot.max_right+2):
		val = grid.get((x, y), 0)
		line += " " if val == 0 else "█"
	print(line)
