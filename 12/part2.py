import re
import itertools
import time

start_time = time.time()

def sign(n):
	return (n>0) - (n<0)

class Axinator:
	def __init__(self, pos):
		self.pos = pos
		self.vel = 0

	def update_vel(self, other):
		if self.pos < other.pos:
			self.vel += 1
			other.vel -= 1
		elif self.pos != other.pos:
			self.vel -= 1
			other.vel += 1

	def update_pos(self):
		self.pos += self.vel

	def get_state(self):
		return f"{self.pos},{self.vel} "

	def __repr__(self):
		return f"{self.pos}"

x_axs = []
y_axs = []
z_axs = []
with open("data.dat") as file:
	for line in file:
		pattern = "<x=(.*), y=(.*), z=(.*)>"
		match = re.search(pattern, line)
		x, y, z = match.groups()
		x_axs.append(Axinator(int(x)))
		y_axs.append(Axinator(int(y)))
		z_axs.append(Axinator(int(z)))

class AxHandler:
	def __init__(self, x_axs, y_axs, z_axs):
		self.xs = x_axs
		self.ys = y_axs
		self.zs = z_axs
		self.items = x_axs + y_axs + z_axs
		self.x_groups = list(itertools.combinations(x_axs, 2))
		self.y_groups = list(itertools.combinations(y_axs, 2))
		self.z_groups = list(itertools.combinations(z_axs, 2))
		self.x_origin = self.get_x_state()
		self.y_origin = self.get_y_state()
		self.z_origin = self.get_z_state()

	def update(self):
		for x1, x2 in self.x_groups:
			x1.update_vel(x2)
		for y1, y2 in self.y_groups:
			y1.update_vel(y2)
		for z1, z2 in self.z_groups:
			z1.update_vel(z2)

		for item in self.items:
			item.update_pos()

	def get_x_state(self):
		return "".join([x.get_state() for x in self.xs])

	def get_y_state(self):
		return "".join([y.get_state() for y in self.ys])

	def get_z_state(self):
		return "".join([z.get_state() for z in self.zs])

	def __repr__(self):
		s = ""
		for i in range(len(self.xs)):
			s += f"""
				pos=<x={self.xs[i].pos:2.0f}, y={self.ys[i].pos:2.0f}, z={self.zs[i].pos:2.0f}>,
				vel=<x={self.xs[i].vel:2.0f}, y={self.ys[i].vel:2.0f}, z={self.zs[i].vel:2.0f}>\n
			"""
		return s
ax_murderer = AxHandler(x_axs, y_axs, z_axs)

x_loops = False
y_loops = False
z_loops = False
loops = 0
while not (x_loops and y_loops and z_loops):
	ax_murderer.update()
	loops += 1
	if ax_murderer.get_x_state() == ax_murderer.x_origin and not x_loops:
		x_loops = loops
	if ax_murderer.get_y_state() == ax_murderer.y_origin and not y_loops:
		y_loops = loops
	if ax_murderer.get_z_state() == ax_murderer.z_origin and not z_loops:
		z_loops = loops

def lcm(num_list):
	# Recursively solve for each set of two values
	if len(num_list) == 1:
		return num_list[0]
	a = num_list.pop()
	b = lcm(num_list)

	# Make sure b >= a
	if a > b:
		a = a+b
		b = a-b
		a = a-b

	# Keep start values
	a_start = a
	b_start = b

	# Search for lcm
	while True:
		a += a_start*int((b-a)/a_start)
		if a == b:
			return a
		b += b_start

print(lcm([x_loops, y_loops, z_loops]), f"Time: {time.time() - start_time:.3f}")


"""
Time:
initial                    -> python3: 2.735 s, pypy3: N/A
homemade lcm               -> python3: 2.854 s, pypy3: 0.447 s
better axinator update_vel -> python3: 3.237 s, pypy3: 0.518 s (?)
better AxHandler update    -> python3: 3.036 s, pypy3: 0.407 s
nvm, no fancy sign thing   -> python3: 2.304 s, pypy3: 0.339 s
"""
