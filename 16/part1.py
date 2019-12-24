import time
import numpy as np

def pattern_value(i, n):
	return [0, 1, 0, -1][(i//n)%4]

start_time = time.time()

signal = open("data.dat", "r").readline().replace("\n", "")
signal_length = len(signal)
signal = np.matrix([int(v) for v in signal]).getT()

start_pattern_time = time.time()
pattern = np.array(0)
pattern.resize(signal_length, signal_length)
pattern = np.matrix(pattern)
for n in range(1, signal_length+1):
	pattern[:][n-1] = [pattern_value(i, n) for i in range(1, signal_length+1)]
print(f"Pattern made in {time.time() - start_pattern_time:.3f} seconds")

start_multi_time = time.time()
for i in range(100):
	signal = np.matrix([abs(v)%10 for v in (pattern*signal).getA1()]).getT()
print(f"Signal decoded in {time.time() - start_multi_time:.3f} seconds")

print(f"Finished in {time.time() - start_time:.3f} seconds")
print("".join(str(v) for v in signal.getA1()[:8]))


"""
optimalization:
start:  python -> 13.1s, pypy -> 1.5s
matrix: python -> 0.13s, pypy -> N/A
"""
