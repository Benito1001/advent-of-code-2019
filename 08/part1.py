with open("data.dat") as infile:
	data = str(infile.readline().strip())


width = 25
height = 6
layer_count = int(len(data)/(width*height))

image = {}
line = 0
layer = 0
for vals in [data[i:i+width] for i in range(0, len(data), width)]:
	if line >= height:
		line = 0
		layer += 1
	if line == 0:
		image[layer] = []
	image[layer].append(vals)
	line += 1

def print_image(image):
	for layer in image.keys():
		print(f"Layer: {layer}")
		for line in image[layer]:
			print(line)
		print()

print_image(image)

digit_count_ray = []
for layer in image.keys():
	digit_count = {"0": 0, "1": 0, "2": 0}
	for line in image[layer]:
		for number in line:
			if digit_count.get(number) is not None:
				digit_count[number] += 1
	digit_count_ray.append(digit_count)

min = 999999; answer_sum = 0
for digit_count in digit_count_ray:
	if digit_count["0"] < min:
		min = digit_count["0"]
		answer_sum = digit_count["1"] * digit_count["2"]

print(min, answer_sum)
