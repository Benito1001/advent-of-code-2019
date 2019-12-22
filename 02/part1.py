intcode = list(eval(open("data.dat", "r").readline()))

intcode[1] = 12
intcode[2] = 2

i = 0
while i < len(intcode):
	if intcode[i] == 1:
		intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
		i += 4
	elif intcode[i] == 2:
		intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
		i += 4
	elif intcode[i] == 99:
		break
	else:
		print(":)")
		break

print(intcode)
