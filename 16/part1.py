import time

take_time = True

signal = open("data.dat", "r").readline().replace("\n", "")

start_pattern = [0, 1, 0, -1]

def extend(pattern):
	repetitions = int(len(pattern)/4 + 1)
	return [0]*repetitions + [1]*repetitions + [0]*repetitions + [-1]*repetitions

start_time = time.time()
for i in range(100):
	new_signal = ""
	pattern = start_pattern.copy()
	for k in range(len(signal)):
		s = 0
		for index, num in enumerate(signal):
			s += int(num)*pattern[(index+1)%len(pattern)]
		new_signal += str(s)[-1]
		pattern = extend(pattern)
	frac = (i+1)/100
	if take_time:
		time_frac = (time.time() - start_time)*(1/frac)
		take_time = False
	print(f"\r{i+1}%, time remaining: {time_frac*(1-frac):.1f} seconds", end="")
	signal = new_signal

print("\n"+signal[:8])
