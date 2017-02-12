from heap import MinHeap

max_size = 101

class Coord:
    def __init__(self, x, y):
        self.x=x
        self.y=y
	
	def __str__(self):
		return str(self.x) + ", " + str(self.y)

    def __lt__(self, other):
        return self.distance < other.distance

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

class PathFinder:
    def __init__(self, maze_file):
        self.close = dict()
        self.open = MinHeap()
        self.grid = []
        self.start_state = None
        self.goal_state = None
        for i in range(max_size):
            self.grid.append([])
        with open(maze_file, 'r') as f:
            line_row = 0
            for line in f:
                line = line.rstrip()
                if not line:
                    continue
                if not self.start_state:
                    self.start_state = line_to_coord(line)
                    continue
                if not self.goal_state:
                    self.goal_state = line_to_coord(line)
                    continue
                for pos in line:
                    self.grid[line_row].append(True if pos == '1' else False)
                line_row += 1


    def find_path(self, start, goal, path):
        path += start
        if start == goal:
            return path
        self.close[start] = True
        neighbors = self.ComputerValidNeighbors(start)
        for n in neighbors:
            if self.maze[n.x][n.y]:
                continue
            n.distance = self.calculate_manhattan_distance(n, goal)
            self.open.insert(n)
        nextC = self.open.extract()
        return self.FindPath(nextC, goal, path)

    def calculate_manhattan_distance(self, start, end):
        return abs(start.x - end.x) + abs(start.y - end.y)

    def compute_valid_neighbors(self, start):
        neighbors = {}
        # Find all neighbors.
        if start.x - 1 >= 0:
            n = Coord(start.x - 1, start.y)
            if not self.close[n]:
                neighbors += n

            if start.y - 1 >= 0:
                n = Coord(start.x - 1, start.y - 1)
                if not self.close[n]:
                    neighbors += n

            if start.y + 1 < max_size:
                n = Coord(start.x - 1, start.y + 1)
                if not self.close[n]:
                    neighbors += n

        if start.y - 1 >= 0:
            n = Coord(start.x, start.y - 1)
            if not self.close[n]:
                neighbors += n

        if start.y + 1 < max_size:
            n = Coord(start.x, start.y + 1)
            if not self.close[n]:
                neighbors += n

        if start.x + 1 < max_size:
            n = Coord(start.x + 1, start.y)
            if not self.close[n]:
                neighbors += n

            if start.y - 1 >= 0:
                n = Coord(start.x + 1, start.y - 1)
                if not self.close[n]:
                    neighbors += n

            if start.y + 1 < max_size:
                n = Coord(start.x + 1, start.y + 1)
                if not self.close[n]:
                    neighbors += n

def line_to_coord(line):
	val = [int(x) for x in line.split(",")]
	if len(val) != 2:
		raise ValueError
	return Coord(val[0], val[1])

