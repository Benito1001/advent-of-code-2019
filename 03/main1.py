import time as timelib

data = open("data.dat", "r")
print("data got!")

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
print("paths got!")

start = timelib.time()
time = None
collisions = []
count = 0
for i in range(len(wire_paths) - 1):
	for pos1 in wire_paths[i]:
		for pos2 in wire_paths[i+1]:
			if pos1 == pos2 and pos1 != (0, 0):
				frac = count/(len(wire_paths[i])*len(wire_paths[i+1]))
				if not time:
					time = (timelib.time() - start)*(1/frac)
				print(pos1, f"{frac*100:.1f}% - Total time: {time:.1f} seconds - {count}/{len(wire_paths[i])*len(wire_paths[i+1])}")
				collisions.append(pos1)
			count += 1

print("\n", f"collisions got in {(timelib.time() - start):.1f} seconds")

distance = min([abs(collision[0]) + abs(collision[1]) for collision in collisions])
print(distance)

# Python3: 1780.5 seconds
# PyPy: 38.7 seconds
