orbits = {}

# Get data

with open("data.dat") as file:
	for line in file:
		info = line.replace("\n", "").split(")")
		body = info[0]
		moon = info[1]
		if not orbits.get(body):
			orbits[body] = {}
		orbits[body][moon] = {}


# Structure data

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


# Print data

symbol_dict = {0: "-", 1: "·", 2:"*"}
def orb_print(orbit, depth=0):
	for key, value in orbit.items():
		print(f"{' '*depth*2}{symbol_dict[depth%3]} {key}", depth)
		orb_print(value, depth+1)
# orb_print(orbits)


# Get path

def orb_get_pathdata(orbit, path = [], return_data = {"YOU":"", "SAN":""}):
	for key, value in orbit.items():
		if key == "YOU" or key == "SAN":
			return_data[key] = path
		else:
			new_path = path.copy()
			new_path.append(key)
			return_data = orb_get_pathdata(value, new_path)
	return return_data

path_data = orb_get_pathdata(orbits["COM"], ["COM"])
YOU_path, SAN_path = path_data["YOU"], path_data["SAN"]


# Get trafer path

transfer_path = []
for i in range(len(YOU_path)):
	if YOU_path[i] != SAN_path[i]:
		transfer_path = YOU_path[i:][::-1] + [YOU_path[i-1]] + SAN_path[i:]
		break


# Print answer

print(transfer_path, len(transfer_path)-1)
