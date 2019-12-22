import re
from vector import Vector3

class Moon:
	def __init__(self, x, y, z):
		self.pos = Vector3(x, y, z)
		self.vel = Vector3()

	def __repr__(self):
		return f"pos = {str(self.pos)}, vel = {str(self.vel)}"

	def update_vel(self):
		for moon in moons:
			if moon == self: continue

			if self.pos.x < moon.pos.x:
				self.vel.x += 1
			elif self.pos.x != moon.pos.x:
				self.vel.x -= 1

			if self.pos.y < moon.pos.y:
				self.vel.y += 1
			elif self.pos.y != moon.pos.y:
				self.vel.y -= 1

			if self.pos.z < moon.pos.z:
				self.vel.z += 1
			elif self.pos.z != moon.pos.z:
				self.vel.z -= 1

	def update_pos(self):
		self.pos += self.vel

	def total_energy(self):
		return sum(abs(self.pos))*sum(abs(self.vel))

moons = []
with open("data.dat") as file:
	for line in file:
		pattern = "<x=(.*), y=(.*), z=(.*)>"
		match = re.search(pattern, line)
		moons.append(Moon(*[int(v) for v in match.groups()]))

for i in range(11):
	print(f"After {i} steps:")
	for moon in moons:
		print(moon)
		moon.update_vel()
	for moon in moons:
		moon.update_pos()
	print()

print(sum([moon.total_energy() for moon in moons]))
