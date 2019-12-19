import time as timelib

data = open("data.dat", "r")
print("data got!")

dir_dict = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
path_pont_dict = {}
collisions = []

start = timelib.time()
id = 0
for wire_data in data:
	wire = wire_data.replace("\n", "").split(",")
	x = 0
	y = 0
	location_ray = [(x, y)]
	for side in wire:
		direction = dir_dict[side[0]]
		steps = int(side[1:])
		for n in range(steps):
			# x-axis
			if direction[0] != 0:
				x += 1*direction[0]
			# y-axis
			else:
				y += 1*direction[1]
			if path_pont_dict.get((x, y)) != None:
				# Don't colide with self
				if not path_pont_dict.get((x, y))[0] == id:
					collisions.append((x, y))
					path_pont_dict[(x, y)] = (id, True)
			else:
				path_pont_dict[(x, y)] = (id, True)
	id += 1
data.close()

print("\n", f"collisions got in {(timelib.time() - start):.10f} seconds")

distance = min([abs(collision[0]) + abs(collision[1]) for collision in collisions])
print(distance)

# Python3: 0.2
# PyPy: 0.2
