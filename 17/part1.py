from intcomputer import IntcodeComputer
intcode = list(eval(open("data.dat", "r").readline()))

ascii_dict = {35: "█", 46: " ", 10: "\n", 60: "<", 62: ">", 94: "^", }

map = ""
def output_func(val):
	global map
	map += ascii_dict[val]

computer = IntcodeComputer(intcode, input, output_func)
computer.run()

grid = [list(row) for row in map.split("\n")]

def is_intersection(pos):
	x = pos[0]; y = pos[1]
	scaffold = ascii_dict[35]

	try:
		if grid[y+1][x] == scaffold and grid[y-1][x] == scaffold:
			if grid[y][x-1] == scaffold and grid[y][x+1] == scaffold:
				return True
	except IndexError:
		return False
	return False

intersections = []
for y, row in enumerate(grid):
	for x, v in enumerate(row):
		if v == ascii_dict[35]:
			if is_intersection((x, y)):
				intersections.append((x, y))
				grid[y][x] = "\033[31m█\033[0m"

print(intersections)

print("".join(["".join(row+["\n"]) for row in grid]))

print(sum([intersection[0]*intersection[1] for intersection in intersections]))
