class IntcodeComputer:
	def __init__(self, intcode, input_func, output_func):
		self.intcode = intcode
		self.output = None
		self.relative_base = 0
		self.get_input = input_func
		self.set_output = output_func
		self.running = True

	def get_value(self, mode, i):
		if mode == 0:
			return self.memory.get(self.memory.get(i, 0), 0)
		elif mode == 1:
			return self.memory.get(i, 0)
		return self.memory.get(self.memory.get(i, 0) + self.relative_base, 0)

	def set_value(self, mode, i, val):
		if mode == 0:
			self.memory[self.memory.get(i, 0)] = val
		else:
			self.memory[self.memory.get(i, 0) + self.relative_base] = val

	def run(self):
		self.memory = {i: self.intcode[i] for i in range(len(self.intcode))}
		i = 0
		while i < len(self.intcode) and self.running:
			operation = str(self.intcode[i]).zfill(5)
			instruction = int(operation[-2:])
			A, B, C = [int(v) for v in operation[:3]]

			if instruction == 1 or instruction == 2:
				val1 = self.get_value(C, i+1)
				val2 = self.get_value(B, i+2)
				self.set_value(A, i+3, val1 + val2 if instruction == 1 else val1 * val2)
				i += 4
			elif instruction == 3:
				self.set_value(C, i+1, self.get_input())
				i += 2
			elif instruction == 4:
				value = self.get_value(C, i+1)
				self.set_output(value)
				i += 2
			elif instruction == 5 or instruction == 6:
				val1 = self.get_value(C, i+1)
				val2 = self.get_value(B, i+2)
				bool = val1 != 0 if instruction == 5 else val1 == 0
				if bool:
					i = val2
				else:
					i += 3
			elif instruction == 7 or instruction == 8:
				val1 = self.get_value(C, i+1)
				val2 = self.get_value(B, i+2)
				bool = val1 < val2 if instruction == 7 else val1 == val2
				self.set_value(A, i+3, 1 if bool else 0)
				i += 4
			elif instruction == 9:
				self.relative_base += self.get_value(C, i+1)
				i += 2
			elif instruction == 99:
				break
			else:
				print("lamao, shit's broken", self.intcode)
				break
