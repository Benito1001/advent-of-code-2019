import time
import numpy as np
import random

def lcm(num_list):
	# Recursively solve for each set of two values
	if len(num_list) == 1:
		return num_list[0]
	a = num_list.pop()
	b = lcm(num_list)

	# Make sure b >= a
	if a>b:
		a = a+b
		b = a-b
		a = a-b

	# Keep start values
	a_start = a
	b_start = b

	# Search for lcm
	while True:
		a += a_start*((b-a)//a_start)
		if a == b:
			return a
		b += b_start

nums = [random.randint(3, 10) for i in range(500)]

np_start = time.time()
val = np.lcm.reduce(nums)
print(val, f"Custom numpy: {time.time() - np_start:.9f}")

custom_start = time.time()
val = lcm(nums)
print(val, f"Custom time: {time.time() - custom_start:.9f}")
