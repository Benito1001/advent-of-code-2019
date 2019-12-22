import time

start = 130254
stop = 678275
num_range = range(start, stop+1)

start_time = time.time()
pass_num = 0
for n in num_range:
	n_str = str(n)
	adjacent = False
	increasing = True
	for i, d in enumerate(n_str[:-1]):
		if not adjacent and d == n_str[i+1]:
			adjacent = True
		if d > n_str[i+1]:
			increasing = False
	if adjacent and increasing:
		pass_num += 1

print(pass_num, f"{time.time() - start_time:.3f}")
