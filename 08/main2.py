with open("data.dat") as infile:
	data = str(infile.readline().strip())


width = 25
height = 6
layer_count = int(len(data)/(width*height))

raw_image = {}
line = 0
layer = 0
for vals in [data[i:i+width] for i in range(0, len(data), width)]:
	if line >= height:
		line = 0
		layer += 1
	if line == 0:
		raw_image[layer] = []
	raw_image[layer].append(vals)
	line += 1


image = [[-1]*width for i in range(height)]
for layer in raw_image.values():
	for y, line in enumerate(layer):
		for x, num in enumerate(line):
			if int(num) != 2 and image[y][x] == -1:
				image[y][x] = "█" if int(num) == 1 else " "

for layer in image:
	print("".join([str(v) for v in layer]))
