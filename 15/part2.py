import time
from intcomputer import IntcodeComputer
from A_star import Grid, A_star
intcode = list(eval(open("data.dat", "r").readline()))

init = True
pos = [0, 0]
direction = 1
turn_left_dict = {1: 3, 2: 4, 3: 2, 4: 1}
turn_right_dict = {1: 4, 2: 3, 3: 1, 4: 2}
reverse_dict = {1: 2, 2: 1, 3: 4, 4: 3}
world_map = {}
current_step = ""

def move(pos, direction):
	pos = pos.copy()
	if direction == 1:
		pos[1] += 1
	elif direction == 2:
		pos[1] -= 1
	elif direction == 3:
		pos[0] -= 1
	else:
		pos[0] += 1
	return pos

minY, minX = float("Infinity"), float("Infinity")
maxY, maxX = -float("Infinity"), -float("Infinity")
def update_border(pos):
	global minY, minX, maxY, maxX
	minY = min(pos[1], minY)
	maxY = max(pos[1], maxY)
	minX = min(pos[0], minX)
	maxX = max(pos[0], maxX)

def input_func():
	global pos
	if init:
		pos = move(pos, direction)
		return direction
	if current_step == "test left":
		pos = move(pos, turn_left_dict[direction])
		return turn_left_dict[direction]
	pos = move(pos, direction)
	return direction

def output_func(value):
	global init, computer, pos, current_step, direction
	global turn_left_dict, turn_right_dict, reverse_dict, world_map

	update_border(pos)
	world_map[tuple(pos)] = value

	if pos == [0, 0]:
		computer.running = False
	if init and value == 0:
		pos = move(pos, reverse_dict[direction])
		direction = turn_right_dict[direction]
		current_step = "move forward"
		init = False
	elif not init:
		if value == 0:
			if current_step == "test left":
				pos = move(pos, reverse_dict[turn_left_dict[direction]])
				current_step = "move forward"
			else:
				pos = move(pos, reverse_dict[direction])
				direction = turn_right_dict[direction]
		elif value == 1:
			if current_step == "test left":
				direction = turn_left_dict[direction]
				current_step = "move forward"
			else:
				current_step = "test left"

computer = IntcodeComputer(intcode, input_func, output_func)
computer.run()
world_map[(0, 0)] = "S"


# Create a grid from the map discovered by the computer:

grid = Grid(maxX - minX + 1, maxY-minY + 1)
graphic_dict = {0: grid.block_tile, 1: grid.space_tile, 2: "O", "S": "S"}
for node in world_map:
	if graphic_dict[world_map[node]] == "O":
		oxygen = (node[0] - minX, node[1] - minY)
	grid[(node[0] - minX, node[1] - minY)] = graphic_dict[world_map[node]]


# Fill grid with oxygen and count time steps

time_steps = -1
edge_oxygens = [oxygen]
while len(edge_oxygens) > 0:
	for oxygen in edge_oxygens.copy():
		for node in grid.adjecents(oxygen):
			if grid[node] != "O":
				edge_oxygens.append(node)
				grid[node] = "O"
		edge_oxygens.remove(oxygen)
	time_steps += 1

print(time_steps)
