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

bot_pos = (0, 0)
for y, row in enumerate(grid):
	for x, v in enumerate(row):
		if v == "^":
			bot_pos = (x, y)

print(map)
print(bot_pos)
