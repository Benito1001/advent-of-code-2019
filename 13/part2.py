from intcomputer import IntcodeComputer

intcode = list(eval(open("data.dat", "r").readline()))
intcode[0] = 2

tile_dict = {0: " ", 1: "█", 2: "#", 3: "╬", 4: "Θ"}
things_dict = {}

player_pos = 0
ball_pos = 0

out_list = []
def output_func(value):
	global out_list, player_pos, ball_pos
	out_list.append(value)
	if len(out_list) == 3:
		if out_list[2] == 3:
			player_pos = out_list[0]
		elif out_list[2] == 4:
			ball_pos = out_list[0]
		things_dict[(out_list[0], out_list[1])] = tile_dict.get(out_list[2], str(out_list[2]))
		out_list = []

def draw_game():
	w = 0
	h = 0
	for key in things_dict:
		w = max(w, key[0])
		h = max(h, key[1])
	for y in range(h+1):
		s = ""
		for x in range(w+2):
			s += things_dict.get((x, y), things_dict.get((-1, y), " "))
		print(s)

def input_func():
	if player_pos > ball_pos:
		return -1
	elif player_pos < ball_pos:
		return 1
	return 0

computer = IntcodeComputer(intcode, input_func, output_func)
computer.run()
draw_game()
