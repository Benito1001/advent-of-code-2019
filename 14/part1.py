import math

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

storage = {}

def make(reaction, amount):
	# Make product
	storage[reaction.output.name] = storage.get(reaction.output.name, 0) + reaction.output.cost*amount

	# What is needed
	for input in reaction.inputs:
		# Make requires resources
		if reactions.get(input.name) != None:
			# How much?
			in_storage = storage.get(input.name, 0)
			new_reaction = reactions[input.name]
			output_count = new_reaction.output.cost
			create_amount = math.ceil((input.cost*amount-in_storage)/output_count)

			make(new_reaction, create_amount)

		# Consume resources
		storage[input.name] = storage.get(input.name, 0) - input.cost*amount



make(reactions["FUEL"], 1)
print(storage)
print(abs(storage["ORE"]))
