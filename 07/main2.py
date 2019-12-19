import itertools

intcode = list(eval(open("data.dat", "r").readline()))

class AmpIntComputer:
	def __init__(self, intcode = []):
		self.og_intcode = intcode
		self.intcode = intcode.copy()
		self.i = 0

	def advance(self, input):
		intcode = self.intcode

		while self.i < len(intcode):
			operation = str(intcode[self.i]).zfill(5)
			instruction = int(operation[-2:])
			A, B, C = [int(v) for v in operation[:3]]

			if instruction == 1 or instruction == 2:
				val1 = intcode[self.i+1] if C == 1 else intcode[intcode[self.i+1]]
				val2 = intcode[self.i+2] if B == 1 else intcode[intcode[self.i+2]]
				intcode[intcode[self.i+3]] = val1 + val2 if instruction == 1 else val1 * val2
				self.i += 4

			elif instruction == 3:
				value = input[0]
				input.remove(value)
				intcode[intcode[self.i+1]] = value
				self.i += 2

			elif instruction == 4:
				value = intcode[self.i+1] if C == 1 else intcode[intcode[self.i+1]]
				self.i += 2
				return value

			elif instruction == 5 or instruction == 6:
				val1 = intcode[self.i+1] if C == 1 else intcode[intcode[self.i+1]]
				val2 = intcode[self.i+2] if B == 1 else intcode[intcode[self.i+2]]
				bool = val1 != 0 if instruction == 5 else val1 == 0
				if bool:
					self.i = val2
				else:
					self.i += 3

			elif instruction == 7 or instruction == 8:
				val1 = intcode[self.i+1] if C == 1 else intcode[intcode[self.i+1]]
				val2 = intcode[self.i+2] if B == 1 else intcode[intcode[self.i+2]]
				bool = val1 < val2 if instruction == 7 else val1 == val2
				intcode[intcode[self.i+3]] = 1 if bool else 0
				self.i += 4

			elif instruction == 99:
				return False

			else:
				print("lamao, shit's broken", intcode)
				break

	def reset(self):
		self.i = 0
		self.intcode = self.og_intcode.copy()

class AmpHandeler:
	def __init__(self, amp_list):
		self.amps = amp_list

	def amp_init(self, inti_tuple):
		next_value = 0
		for i, amp in enumerate(self.amps):
			next_value = amp.advance([inti_tuple[i], next_value])
		self.last_value = next_value

	def run(self):
		next_value = self.last_value
		while next_value:
			prev_value = next_value
			for amp in self.amps:
				next_value = amp.advance([next_value])
		return prev_value

	def reset(self):
		for amp in self.amps:
			amp.reset()

amp_handeler = AmpHandeler([AmpIntComputer(intcode.copy()) for i in range(5)])

results = []
for permutation in itertools.permutations([5, 6, 7, 8, 9]):
	amp_handeler.amp_init(permutation)
	results.append(amp_handeler.run())
	amp_handeler.reset()
print(max(results))
