class Grid:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.path_tile = "\033[32m*\033[0m"
		self.block_tile = "\033[31m█\033[0m"
		self.tested_tile = "\033[30m█\033[0m"
		self.space_tile = " "
		self.tiles = [[self.space_tile for i in range(width)] for j in range(height)]

	def __getitem__(self, index):
		if hasattr(index, "__getitem__"):
			if len(index) == 2:
				return self.tiles[index[1]][index[0]]
			else:
				raise IndexError(f"Invalid subscript {index}")
		else:
			return self.tiles[index]

	def __setitem__(self, index, value):
		if hasattr(index, "__getitem__") and len(index) == 2:
			self.tiles[index[1]][index[0]] = value
		else:
			raise IndexError(f"Invalid subscript {index}")

	def adjecents(self, pos):
		tiles = []
		if pos[0] > 0:
			tiles.append((pos[0]-1, pos[1]))
		if pos[0] < self.width-1:
			tiles.append((pos[0]+1, pos[1]))
		if pos[1] > 0:
			tiles.append((pos[0], pos[1]-1))
		if pos[1] < self.height-1:
			tiles.append((pos[0], pos[1]+1))
		for tile in tiles:
			if self[tile] != self.block_tile:
				yield tile

	def colorize(self, path):
		for node in path:
			self[node] = self.path_tile

	def __repr__(self):
		s = "┌" + "─"*self.width + "┐\n"
		for y in range(self.height):
			s += "│"
			for x in range(self.width):
				s += self[(x, y)]
			s += "│\n"
		s += "└" + "─"*self.width + "┘"
		return s

def dist_between(point1, point2):
	return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def A_star(start, goal, grid, h):
	# should maybe return new colorized grid instead of change parameter grid
	open_list = [start]
	came_from = {}

	# gScore[node] is the cost of the cheapest known path from start to that node.
	gScore = {}
	gScore[start] = 0

	# fScore[node] = gScore[node] + h(node).
	fScore = {}
	fScore[start] = h(start)

	while len(open_list) > 0:
		# get the node in open_list with the lowest fScore
		min_value = float("Infinity")
		for node in open_list:
			if fScore[node] < min_value:
				min_value = fScore[node]
				current = node

		# if the goal is reached, return the path
		if current == goal:
			path = []
			while came_from.get(current) is not None:
				path.append(current)
				current = came_from[current]
			grid.colorize(path)
			grid[start] = "S"
			grid[goal] = "G"
			return path

		grid[current] = grid.tested_tile
		open_list.remove(current)
		for neighbor in grid.adjecents(current):
			# tentative_gScore is the distance from start to the neighbor through current
			tentative_gScore = gScore[current] + dist_between(current, neighbor)
			if tentative_gScore < gScore.get(neighbor, float("Infinity")):
				# this path to neighbor is better than any previous one
				came_from[neighbor] = current
				gScore[neighbor] = tentative_gScore
				fScore[neighbor] = gScore[neighbor] + h(neighbor)
				if open_list.count(neighbor) == 0:
					open_list.append(neighbor)

	# open set is empty but goal was never reached
	print("No route found")


if __name__ == '__main__':
	start = (0, 0)
	goal = (9, 9)
	map_width = 10
	map_height = 10

	map = Grid(map_width, map_height)
	map[start] = "S"
	map[goal] = "G"
	for x in range(5):
		map[(x, 4)] = map.block_tile
	for y in range(3):
		map[(4, 2+y)] = map.block_tile
	for x in range(8):
		map[(2+x, 7)] = map.block_tile

	def dist_to_goal(point):
		return dist_between(point, goal)

	print(map)
	shortest_path = A_star(start, goal, map, dist_to_goal)
	print(map)
