signal = open("data.dat", "r").readline().replace("\n", "")*10000
skip_count = int(signal[:7])

signal = [int(v) for v in signal[skip_count:]]
signal_length = len(signal)

for i in range(100):
	new_signal = [0]*signal_length
	partial_sum = 0
	for j in range(1, signal_length+1):
		partial_sum += signal[-j]
		new_signal[-j] = abs(partial_sum)%10
	signal = new_signal

print("".join([str(v) for v in signal[:8]]))
