intcode = list(eval(open("data.dat", "r").readline()))

i = 0
while i < len(intcode):
	operation = str(intcode[i]).zfill(5)
	instruction = int(operation[-2:])
	A, B, C = [int(v) for v in operation[:3]]

	if instruction == 1 or instruction == 2:
		val1 = intcode[i+1] if C == 1 else intcode[intcode[i+1]]
		val2 = intcode[i+2] if B == 1 else intcode[intcode[i+2]]
		intcode[intcode[i+3]] = val1 + val2 if instruction == 1 else val1 * val2
		i += 4
	elif instruction == 3:
		intcode[intcode[i+1]] = int(input("Gimmi a number boi: "))
		i += 2
	elif instruction == 4:
		value = intcode[i+1] if C == 1 else intcode[intcode[i+1]]
		print(value)
		i += 2
	elif instruction == 5 or instruction == 6:
		val1 = intcode[i+1] if C == 1 else intcode[intcode[i+1]]
		val2 = intcode[i+2] if B == 1 else intcode[intcode[i+2]]
		bool = val1 != 0 if instruction == 5 else val1 == 0
		if bool:
			i = val2
		else:
			i += 3
	elif instruction == 7 or instruction == 8:
		val1 = intcode[i+1] if C == 1 else intcode[intcode[i+1]]
		val2 = intcode[i+2] if B == 1 else intcode[intcode[i+2]]
		bool = val1 < val2 if instruction == 7 else val1 == val2
		intcode[intcode[i+3]] = 1 if bool else 0
		i += 4
	elif instruction == 99:
		break
	else:
		print("lamao, shit's broken", intcode)
		break
