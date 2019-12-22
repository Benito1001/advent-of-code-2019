import math
import numpy as np

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

	def get_square_dist(self):
		return self.x**2 + self.y**2

	def __str__(self):
		return f"[{self.x}, {self.y}]"

station = Point(23, 19)
station_sight_values = []

with open("data.dat") as file:
	for y, line in enumerate(file):
		for x, val in enumerate(line):
			if val == "#" and (x, y) != station.get_values():
				ast_vec = Vector(station, Point(x, y))
				ast_vec.y *= -1
				station_sight_values.append({"angle": ast_vec.get_angle(), "distance": ast_vec.get_square_dist(), "pos": (x, y)})

angle = math.pi/2
i = 1
while len(station_sight_values) - 1 != 0:
	target = sorted(filter(lambda dict: dict["angle"] == angle, station_sight_values), key=lambda dict: dict["distance"])[0]
	station_sight_values.remove(target)
	print(i, target["pos"])
	next_target = list(filter(lambda dict: dict["angle"] < angle, station_sight_values))
	if len(next_target) == 0:
		next_target = list(filter(lambda dict: dict["angle"] <= angle % (math.pi*2), station_sight_values))
		if len(next_target) == 0:
			next_target = station_sight_values
	angle = sorted(next_target, key=lambda dict: dict["angle"], reverse=True)[0]["angle"]
	i += 1
