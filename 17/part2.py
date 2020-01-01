import numpy as np
import itertools
from classes import Grid, Bot
from intcomputer import IntcodeComputer
intcode = list(eval(open("data.dat", "r").readline()))

ascii_dict = {35: "█", 46: " ", 10: "\n", 94: "^"}


# Get grid

map = ""
def output_func(val):
	global map
	map += ascii_dict[val]

computer = IntcodeComputer(intcode, input, output_func)
computer.run()

grid = Grid([list(row) for row in map[:-2].split("\n")])


# Get bot pos

bot = Bot()
for y, row in enumerate(grid):
	for x, v in enumerate(row):
		if v == "^":
			bot.pos = np.array((x, y))


# Get bot path

bot_path = []
new_dir = None
while new_dir != "END":
	grid[bot.pos] = "B"
	new_dir = bot.change_dir(grid)
	if new_dir != "END":
		bot_path.append(new_dir)
		steps = bot.move_forward(grid)
		bot_path.append(steps)


# Get bot_path parts:


class ListCompressor:
	def __init__(self, list):
		self.list = list
		self.list_parts = self.get_list_parts()
		self.partial_combinations = self.get_partial_combinations()

	def remove(self, list, element):
		while True:
			try:
				list.remove(element)
			except Exception:
				break

	def get_list_parts(self):
		list = self.list.copy()
		list_parts = []
		for element in list:
			list_parts.append(element)
			self.remove(list, element)
		return list_parts

	def get_partial_combinations(self):
		partial_combinations = []
		for i in range(1, len(self.list_parts)):
			for permutation in itertools.permutations(self.list_parts, i):
				partial_combinations.append(list(permutation))
		return partial_combinations

	def is_combination_of(self, item_list):
		i = 0
		while i < len(self.list):
			start_i = i
			for item in item_list:
				fits = True
				for k in range(len(item)):
					if item[k] != self.list[i + k]:
						fits = False
				if fits:
					i += len(item)
					break
			if i == start_i:
				return False
		return True

list_compressor = ListCompressor(bot_path)


print(len(bot_path)/20)
print(list_compressor.list_parts)
# functions must have an avrage length > 3.7
print(len(list_compressor.partial_combinations))

"""
for functions in itertools.combinations(list_compressor.partial_combinations, 3):
	if list_compressor.is_combination_of(functions):
		print(functions)
"""
