def dist_between(point1, point2):
	return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def A_star(start, goal, h, grid):
	"""
	An implementation of the A* algorithm
	start and goal must be subsriptable with x as index 0 and y as index 1
	h is a heuristic function
	grid needs to be an object with a adjecents function that returns possible path candidates
	"""

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
			return path[::-1]

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
