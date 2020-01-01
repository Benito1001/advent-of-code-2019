import math
import re
from grid import Grid
from A_star import A_star

class KeyDoor:
	def __init__(self, char, pos):
		self.char = char
		self.pos = pos

	def __repr__(self):
		return self.char

	def copy(self):
		return KeyDoor(self.char, self.pos)

class KeyDoorList:
	def __init__(self, KeyDoors=None):
		if KeyDoors is None:
			self.KeyDoors = []
		else:
			self.KeyDoors = KeyDoors

	def remove(self, char):
		for KeyDoor in self.KeyDoors:
			if KeyDoor.char == char:
				self.KeyDoors.remove(KeyDoor)
				return KeyDoor.pos

	def __getitem__(self, index):
		return self.KeyDoors[index]

	def __setitem__(self, index, value):
		self.KeyDoors[index] = value

	def __len__(self):
		return len(self.KeyDoors)

	def __repr__(self):
		return ", ".join([str(KeyDoor) for KeyDoor in self.KeyDoors])

	def copy(self):
		return KeyDoorList([KeyDoor.copy() for KeyDoor in self.KeyDoors])

pos = (0, 0)
keys = KeyDoorList()
doors = KeyDoorList()

tiles = []

with open("data.dat") as file:
	for y, line in enumerate(file):
		for x, val in enumerate(line):
			if val == "@":
				pos = (x, y)
			elif re.search("[a-z]", val) is not None:
				keys.KeyDoors.append(KeyDoor(val, (x, y)))
			elif re.search("[A-Z]", val) is not None:
				doors.KeyDoors.append(KeyDoor(val, (x, y)))
		tiles.append(list(line.replace("\n", "")))
grid = Grid(tiles)
key_count = len(keys)
print(key_count)
path_count = math.factorial(key_count)

def create_h(goal):
	def h(tile):
		return abs(tile[0] - goal[0]) + abs(tile[1] - goal[1])
	return h


# TODO: Use recursion and be a good boy to check multiple possibilities. See: minmax type algorithm

possible_paths = []
def find_routes(pos, keys, doors, grid, distance, path):
	if len(keys) == 0:
		global possible_paths, path_count
		possible_paths.append((distance, path+" |"))
		print(f"\r{len(possible_paths)}/{path_count}?", end="")

	# get next key
	for i, key in enumerate(keys):
		key_pos = key.pos
		grid.searching_tile = key.char
		from_pos = A_star(pos, key_pos, create_h(key_pos), grid)
		grid.searching_tile = ":("
		if from_pos is not None:
			# remove key and open door, change grid
			new_keys = keys.copy()
			new_keys.remove(key.char)
			new_grid = grid.copy()
			new_grid[pos] = "."
			new_grid[key.pos] = "@"
			new_doors = doors.copy()
			rem_door = new_doors.remove(key.char.upper())
			if rem_door is not None:
				new_grid[rem_door] = "."

			# find new possible routes
			find_routes(key.pos, new_keys, new_doors, new_grid, distance + len(from_pos), f"{path} {key.char}")
		if distance == 0:
			print(f"\n{i}/{key_count}")


find_routes(pos, keys, doors, grid, 0, "|")
print()
print(len(possible_paths))

shortest_path = ""
shortest_length = float("Infinity")
for path in possible_paths:
	if path[0] < shortest_length:
		shortest_length = path[0]
		shortest_path = path[1]

print(shortest_path, "->", shortest_length)
