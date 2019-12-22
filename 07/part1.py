intcode = list(eval(open("data.dat", "r").readline()))

class IntcodeComputer:
	def __init__(self, intcode = []):
		self.intcode = intcode
		self.instruction = []
		self.output = 0

	def get_input(self):
		return_value = self.instructions[0]
		self.instructions.remove(return_value)
		return return_value

	def set_output(self, value):
		self.output = value

	def run(self):
		intcode = self.intcode.copy()
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
				intcode[intcode[i+1]] = self.get_input()
				i += 2
			elif instruction == 4:
				value = intcode[i+1] if C == 1 else intcode[intcode[i+1]]
				self.set_output(value)
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

	def configurate_amplifier(self, input_ray):
		for i in range(5):
			self.instructions = [input_ray[i], self.output]
			self.run()
		output = self.output
		self.output = 0
		self.instruction = []
		return output

intcode_computer = IntcodeComputer(intcode)


from random import shuffle

wasted_ops = 0
dict = {}
results = []
for n in range(5*4*3*2):
	s = [0, 1, 2, 3, 4]
	shuffle(s)
	input_tuple = tuple([int(e) for e in s])
	while dict.get(input_tuple):
		shuffle(s)
		input_tuple = tuple([int(e) for e in s])
		wasted_ops += 1
	dict[input_tuple] = True
	results.append(intcode_computer.configurate_amplifier(input_tuple))

print(f"Result: {max(results)}")
print(f"Stupid ops: {wasted_ops}")
