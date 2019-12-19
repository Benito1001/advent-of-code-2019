from intcomputer import IntcodeComputer
import time

intcode = list(eval(open("data.dat", "r").readline()))
intcode[0] = 2

tile_dict = {0: " ", 1: "█", 2: "#", 3: "-", 4: "Θ"}
print("\033[2J")

player_pos = 0
ball_pos = 0
score = 0

out_list = []
def output_func(value):
	global out_list, player_pos, ball_pos, score
	out_list.append(value)
	if len(out_list) == 3:
		if out_list[2] == 3:
			player_pos = out_list[0]
		elif out_list[2] == 4:
			ball_pos = out_list[0]

		if tile_dict.get(out_list[2]) == None:
			score = out_list[2]
		else:
			print(f"\033[{out_list[1]+1};{out_list[0]+1}H{tile_dict[out_list[2]]}")

		out_list = []

def input_func():
	time.sleep(1/60)
	if player_pos > ball_pos:
		return -1
	elif player_pos < ball_pos:
		return 1
	return 0

computer = IntcodeComputer(intcode, input_func, output_func)
computer.run()
print("\033[2J")
print(score)
