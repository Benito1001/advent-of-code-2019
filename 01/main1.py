from math import floor

data = open("data.dat", "r")
output = []

for line in data:
	output.append(floor(int(line)/3) - 2)

print(sum(output))
