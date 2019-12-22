import math

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def get_values(self):
		return (self.x, self.y)

class Vector:
	def __init__(self, p0, p1):
		self.x = p1.x - p0.x
		self.y = p1.y - p0.y

	def get_angle(self):
		return math.atan2(self.y, self.x)

asteroids = []
with open("data.dat") as file:
	for y, line in enumerate(file):
		for x, val in enumerate(line):
			if val == "#":
			 	asteroids.append({"pos": Point(x, y), "sight_angles": []})

for asteroid in asteroids:
	for other_asteroid in asteroids:
		if asteroid != other_asteroid:
			ast_angle = Vector(asteroid["pos"], other_asteroid["pos"]).get_angle()
			if asteroid["sight_angles"].count(ast_angle) == 0:
				asteroid["sight_angles"].append(ast_angle)

max = 0
pos = (0, 0)
for asteroid in asteroids:
	if len(asteroid["sight_angles"]) > max:
		max = len(asteroid["sight_angles"])
		pos = asteroid["pos"]

print(max, pos.get_values())
