import random
from collections import deque

class Node(object):
	def __init__(self, x, y):
		self.visited = False
		self.blocked = False
		self.x = x
		self.y = y

	def setBlocked(self):
		self.blocked = True

class Grid(object):
	def __init__(self):
		self.grid = []
		for i in range(101):
			self.grid.append([])
			for j in range(101):
				self.grid[i].append(Node(j, i))
	
	def getNode(x, y):
		return self.grid[y][x]

	def generate_maze(self):
		if not self.grid:
			raise Exception("No grid found")

		self.start_x = random.randint(0, 100)
		self.start_y = random.randint(0, 100)

		self.grid = dfs(self, self.getNode(self.start_x, self.start_y))
		return self 
	
	def find_unexpanded_node(self):
		if not self.grid:
			raise Exception("No grid found")

		for x in range(101):
			for y in range(101):
				if self.getNode(x, y).visited == False:
					return self.getNode(x, y)

		return None 

	def generate_neighbors(self, x, y):
		if not self.grid:
			raise Exception("No grid found")

		for x_ in range(max(0, x-1), min(100, x+1)):
			for y_ in range(max(0, y-1), min(100, y+1)):
				if (x, y) == (x_, y_):
					continue
				yield self.getNode(x_, y_)

def dfs(grid, start):
	visited_set = set()
	stack = deque()
	stack.append(start)

	while len(visited_set) != 101:
		while stack:
			vertex = stack.pop()
			if not vertex.visited:
				if (random.random() * 100) <= 30.0:
					vertex.blocked = True 
				vertex.visited = True
				visited_set.add(vertex)
				for neighbor in grid.generate_neighbors(vertex.x, vertex.y):
					stack.append(neighbor)
		n = grid.find_unexpanded_node()
		if not n:
			break
		stack.append(n)

	grid.getNode(grid.start_x, grid.start_y).blocked = False
	return grid.grid

def main():
	for i in range(50):
		maze_index = i
		if maze_index < 10:
			maze_index = '0' + str(maze_index)
		else:
			maze_index = str(maze_index)
		print "Generating maze " + maze_index
		maze = Grid().generate_maze()
		with open('mazes/maze' + maze_index, 'w') as f:
			# Start state coordinates
			f.write(str(maze.start_x) + "," + str(maze.start_y) + "\n")
			# End state coordinates
			f.write(str(random.randint(0, 100)) + "," + str(random.randint(0, 100)) + "\n")
			for x in range(101):
				for y in range(101):
					coordValue = '0'
					if maze.getNode(x, y).blocked:
						coordValue = '1'
					f.write(coordValue)
				if x != 100:
					f.write('\n')

if __name__ == "__main__":
	main()
