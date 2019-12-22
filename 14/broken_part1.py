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

tree = {}
def swapify(reaction, waste = False):
	inputs_list = reaction.inputs.copy()
	for input in inputs_list:
		chain_reaction = reactions.get(input.name)
		if chain_reaction == None:
			continue
		chain_reaction_cost = chain_reaction.output.cost
		multi = input.cost/chain_reaction_cost
		if waste:
			multi = math.ceil(multi)
		if multi % 1 == 0:
			reaction.inputs.remove(input)
			for chemical in swapify(reactions[input.name]*multi).inputs:
				reaction.inputs.append(chemical)
	return reaction

def fixify(reaction, waste=False):
	changed = True
	while changed:
		changed = False
		new_reaction = swapify(reaction.copy(), waste)
		if reaction != new_reaction:
			reaction = new_reaction.compactify()
			changed = True
	return reaction.compactify()

def wasteify(reaction):
	changed = True
	while changed:
		changed = False
		new_reaction = swapify(reaction.copy(), waste=True)
		new_reaction.compactify()
		if reaction != new_reaction:
			reaction = fixify(new_reaction)
			changed = True
	return reaction

reaction = fixify(reactions["FUEL"])
reaction = wasteify(reaction)
print(reaction.inputs)
