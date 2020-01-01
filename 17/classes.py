import numpy as np

class Grid:
	def __init__(self, list2d):
		self.tiles = list2d
		self.width = len(self.tiles[0])
		self.height = len(self.tiles)

	def __getitem__(self, index):
		if hasattr(index, "__getitem__"):
			if len(index) == 2:
				return self.tiles[index[1]][index[0]]
			else:
				raise IndexError(f"Invalid subscript {index}")
		else:
			return self.tiles[index]

	def __setitem__(self, index, value):
		if hasattr(index, "__getitem__") and len(index) == 2:
			self.tiles[index[1]][index[0]] = value
		else:
			raise IndexError(f"Invalid subscript {index}")

	def get(self, index):
		try:
			return self[index]
		except Exception:
			return " "

	def __repr__(self):
		s = "┌" + "─"*self.width + "┐\n"
		for y in range(self.height):
			s += "│"
			for x in range(self.width):
				s += self[(x, y)]
			s += "│\n"
		s += "└" + "─"*self.width + "┘"
		return s

class Bot:
	def __init__(self, pos=(0, 0), dir=0):
		self.pos = pos
		self.dir = dir

	def turn(self, dir):
		if dir == "L":
			self.dir = (self.dir-1) % 4
		elif dir == "R":
			self.dir = (self.dir+1) % 4

	def step(self, dir=None):
		if dir is None:
			dir = self.dir
		step_dict = {
			0: np.array((0, -1)), 1: np.array((1, 0)),
			2: np.array((0, 1)), 3: np.array((-1, 0))
		}
		self.pos += step_dict[dir]

	def step_back(self):
		self.step((self.dir-2) % 4)

	def change_dir(self, grid):
		self.turn("L")
		self.step()
		if grid.get(self.pos) != " ":
			self.step_back()
			return "L"
		self.step_back()
		self.turn("R")
		self.turn("R")
		self.step()
		if grid.get(self.pos) != " ":
			self.step_back()
			return "R"
		return "END"

	def move_forward(self, grid):
		steps = 0
		while grid.get(self.pos) != " ":
			self.step()
			steps += 1
		self.step_back()
		return steps-1
