from intcomputer import IntcodeComputer
intcode = list(eval(open("data.dat", "r").readline()))

tile_dict = {0: " ", 1: "|", 2: "#", 3: "-", 4: "."}
things_dict = {}

out_list = []
def output_func(value):
	global out_list
	out_list.append(value)
	if len(out_list) == 3:
		# TODO
		things_dict[(out_list[0], out_list[1])] = tile_dict[out_list[2]]
		out_list = []

computer = IntcodeComputer(intcode, input, output_func)
computer.run()

w = 0
h = 0
for key in things_dict:
	w = max(w, key[0])
	h = max(h, key[1])

game_state = ""
for y in range(h+1):
	s = ""
	for x in range(w+1):
		s += things_dict.get((x, y), "9")
	game_state += s + "\n"
print(game_state)
print(game_state.count("#"))
