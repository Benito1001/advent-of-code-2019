from math import floor

data = open("data.dat", "r")
output = []

for line in data:
	fuel_ray = [floor(int(line)/3) - 2]
	while floor(int(fuel_ray[-1])/3) - 2 > 0:
		fuel_ray.append(floor(int(fuel_ray[-1])/3) - 2)
	output.append(sum(fuel_ray))

print(sum(output))
