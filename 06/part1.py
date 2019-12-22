orbits = {}

with open("data.dat") as file:
	for line in file:
		info = line.replace("\n", "").split(")")
		body = info[0]
		moon = info[1]
		if not orbits.get(body):
			orbits[body] = {}
		orbits[body][moon] = {}

#print(orbits)

def orb_swap(sub_orbit):
	swapped = False
	for key in sub_orbit.keys():
		if orbits.get(key) and len(orbits[key].keys()) != 0:
			sub_orbit[key] = orbits[key]
			orbits[key] = {}
			swapped = True
	return swapped

def orb_pass(orbit):
	for sub_orbit in orbit.values():
		if orb_swap(sub_orbit):
			orb_pass(sub_orbit)

orb_pass(orbits)

for key, value in orbits.copy().items():
	if value == {}:
		orbits.pop(key)

symbol_dict = {0: "-", 1: "·", 2:"*"}

def orb_print(orbit, depth):
	for key, value in orbit.items():
		print(f"{' '*depth*2}{symbol_dict[depth%3]} {key}", depth)
		orb_print(value, depth+1)

#orb_print(orbits, 0)

def orb_calc_orbsum(orbit, depth=0, orbsum=0, max_depth=0):
	for key, value in orbit.items():
		orbsum += depth
		orbsum, max_depth = orb_calc_orbsum(value, depth+1, orbsum, max(max_depth, depth))
	return orbsum, max_depth

print(orb_calc_orbsum(orbits))
