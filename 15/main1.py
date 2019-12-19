from intcomputer import IntcodeComputer
intcode = list(eval(open("data.dat", "r").readline()))

init = True

pos = [0, 0]
direction = 1
direction_dict = {1: "north", 2: "south", 3: "west", 4: "east"}
turn_left_dict = {1: 3, 2: 4, 3: 2, 4: 1}
turn_right_dict = {1: 4, 2: 3, 3: 1, 4: 2}
reverse_dict = {1: 2, 2: 1, 3: 4, 4: 3}
graphic_dict = {0: "#", 1:"-", 2:"O"}
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
	# print(pos, current_step, direction_dict[direction], value)
	update_border(pos)
	world_map[tuple(pos)] = graphic_dict[value]
	if value == 2:
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
	# print(pos, current_step, direction_dict[direction], "\n")

computer = IntcodeComputer(intcode, input_func, output_func)
computer.run()
world_map[(0, 0)] = "S"

for y in range(maxY, minY-1, -1):
	s = ""
	for x in range(minX, maxX+1):
		s += world_map.get((x, y), " ")
	print(s)

print(pos)
print(minX, minY, maxX, maxY)
