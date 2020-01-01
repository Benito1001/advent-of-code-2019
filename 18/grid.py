import re

class Grid:
	def __init__(self, list2d):
		self.tiles = list2d
		self.width = len(self.tiles[0])
		self.height = len(self.tiles)
		self.searching_tile = ";)"

	def adjecents(self, pos):
		tiles = []
		if pos[0] > 0:
			tiles.append((pos[0]-1, pos[1]))
		if pos[0] < self.width-1:
			tiles.append((pos[0]+1, pos[1]))
		if pos[1] > 0:
			tiles.append((pos[0], pos[1]-1))
		if pos[1] < self.height-1:
			tiles.append((pos[0], pos[1]+1))
		for tile in tiles:
			if self[tile] == "." or self[tile] == self.searching_tile:
				yield tile

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

	def __repr__(self):
		s = "┌" + "─"*self.width + "┐\n"
		for y in range(self.height):
			s += "│"
			for x in range(self.width):
				s += self[(x, y)]
			s += "│\n"
		s += "└" + "─"*self.width + "┘"
		return s

	def copy(self):
		return Grid([row.copy() for row in self.tiles])
