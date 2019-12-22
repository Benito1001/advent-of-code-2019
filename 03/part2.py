import time as timelib

data = open("data.dat", "r")

dir_dict = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

wire_paths = []
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
			location_ray.append((x, y))
	wire_paths.append(location_ray)
data.close()

start = timelib.time()
time = None
collisions = []
count = 0

path1, path2 = wire_paths
for i, point1 in enumerate(path1):
	for j, point2 in enumerate(path2):
		if point1 == point2 and point1 != (0, 0):
			frac = count/(len(path1)*len(path2))
			if not time:
				time = (timelib.time() - start)*(1/frac)
			print(f"Time remaining: {time*(1-frac):.3f} seconds")
			collisions.append((point1, i+j))
		count += 1

print(f"\ncollisions got in {(timelib.time() - start):.1f} seconds")

distance = min([collision[1] for collision in collisions])
print(distance)

# Python3: 2523.959+ seconds
# PyPy: 45.2 seconds
