import math
import time

reactions = {}

class Reaction:
	def __init__(self, inputs, output):
		self.inputs = inputs
		self.output = output

	def __repr__(self):
		return f"{', '.join(str(input) for input in self.inputs)} => {self.output}"

	def compactify(self):
		for input in self.inputs:
			for i, nother_input in enumerate(self.inputs):
				if input is not nother_input and input.name == nother_input.name:
					input.cost += self.inputs.pop(i).cost
		return self

	def __mul__(self, n):
		inputs = []
		for input in self.inputs:
			inputs.append(input*n)
		return Reaction(inputs, self.output*n)

	def copy(self):
		return Reaction(self.inputs.copy(), self.output.copy())

	def __eq__(self, other):
		if other:
			return self.inputs == other.inputs and self.output == other.output
		return False

	def __neq__(self, other):
		return not self.__eq__(other)

class Chemical:
	def __init__(self, cost, name):
		self.cost = int(cost)
		self.name = name

	def __repr__(self):
		return f"{self.cost} {self.name}"

	def __mul__(self, n):
		return Chemical(self.cost*n, self.name)

	def copy(self):
		return Chemical(self.cost, self.name)

	def __eq__(self, other):
		return self.cost == other.cost and self.name == other.name

	def __neq__(self, other):
		return not self.__eq__(other)

with open("data.dat") as file:
	for line in file:
		inputs, result = line.replace("\n", "").split("=>")
		output_chem = Chemical(*result.split())
		input_chems = [Chemical(*input.split()) for input in inputs.split(",")]
		reactions[output_chem.name] = Reaction(input_chems, output_chem)


def make(reaction, amount, storage):
	# Make product
	storage[reaction.output.name] = storage.get(reaction.output.name, 0) + reaction.output.cost*amount

	# What is needed
	for input in reaction.inputs:
		# If input can be made (is not ORE)
		if reactions.get(input.name) is not None:
			new_reaction = reactions[input.name]
			# How much?
			in_storage = storage.get(input.name, 0)
			output_count = new_reaction.output.cost
			create_amount = math.ceil((input.cost*amount-in_storage)/output_count)
			# Make required resources
			make(new_reaction, create_amount, storage)

		# Consume resources
		storage[input.name] = storage.get(input.name, 0) - input.cost*amount
	return storage

def get_cost(amount):
	storage = make(reactions["FUEL"], amount, {})
	return abs(storage["ORE"])

start_time = time.time()

ORE = 1000000000000

min = 100
max = 200

print(min, max)

loops = [0, 0]
while get_cost(min) < ORE:
	max = max*2
	min = min*2
	loops[0] += 1

cost = 0
while True:
	new_min = max + (min-max)//2
	prev_cost = get_cost(new_min)
	if prev_cost == cost:
		break
	if get_cost(new_min) > ORE:
		min = new_min
	else:
		max = new_min
	cost = prev_cost
	loops[1] += 1

print(max, loops, f"{time.time() - start_time:.3f}")
