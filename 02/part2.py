def get_intcode_value(noun, verb):
	intcode = list(eval(open("data.dat", "r").readline()))
	intcode[1] = noun
	intcode[2] = verb

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

	return intcode[0]

def i_to_noun_verb(i):
	noun = i % 100
	return (i % 100, int((i-noun)/100))

i = 1
intcode_value = get_intcode_value(0, 0)
while intcode_value != 19690720 and i < 9999:
	noun, verb = i_to_noun_verb(i)
	intcode_value = get_intcode_value(noun, verb)
	i += 1

noun, verb = i_to_noun_verb(i-1)
print(100 * noun + verb)
