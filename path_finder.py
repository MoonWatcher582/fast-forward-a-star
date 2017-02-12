from heap import MinHeap

max_size = 101

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = -1

    def __lt__(self, other):
        return self.distance < other.distance

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

class PathFinder:
    def __init__(self, maze_file):
        # TODO: read maze into 2D  array.
        self.close = dict()
        self.open = MinHeap()

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

