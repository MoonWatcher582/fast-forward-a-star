from heap import MinHeap
import sys

max_size = 101

class Coord:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.g=-1
        self.__repr__ = self.__str__

    def __str__(self):
        return "{" + str(self.x) + ", " + str(self.y) + "}"

    def __lt__(self, other):
        return (self.distance + self.g) < (other.distance + other.g)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __hash__(self):
        return hash((self.x, self.y))

class HighCoord:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.g=-1
        self.__repr__ = self.__str__

    def __str__(self):
        return "{" + str(self.x) + ", " + str(self.y) + "}"

    def __lt__(self, other):
        return (self.distance - self.g) < (other.distance - other.g)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __hash__(self):
        return hash((self.x, self.y))

class PathFinderNormal:
    def __init__(self, maze_file):
        self.close = dict()
        self.open = MinHeap()
        self.open_dict = dict()
        self.grid = []
        self.start_state = None
        self.goal_state = None
        for i in range(max_size):
            self.grid.append([])
        with open(maze_file, 'r') as f:
            line_row = 0
            for line in f:
                self.grid.append([])
                line = line.rstrip()
                if not line:
                    continue
                if not self.start_state:
                    self.start_state = line_to_coord(line)
                    self.start_state.g = 0
                    continue
                if not self.goal_state:
                    self.goal_state = line_to_coord(line)
                    continue
                for pos in line:
                    self.grid[line_row].append(True if pos == '1' else False)
                line_row += 1

    def find_path(self):
        return self.find_path_internal(self.start_state, self.goal_state, [])


    def find_path_internal(self, start, goal, path):
        path.append(start)
        if start == goal:
            return path
        self.close[start] = True
        neighbors = self.compute_valid_neighbors(start)
        if neighbors:
            for n in neighbors:
                n.g = start.g + 1
                if self.grid[n.y][n.x]:
                    continue
                n.distance = calculate_manhattan_distance(n, goal)
                self.open.insert(n)
                self.open_dict[n] = True
        nextC = self.open.extract()
        if not nextC:
            return []
        return self.find_path_internal(nextC, goal, path)


    def compute_valid_neighbors(self, start):
        neighbors = []
        # Find all neighbors.
        if start.x - 1 >= 0:
            n = Coord(start.x - 1, start.y)
            if not self.close.has_key(n):
                neighbors.append(n)

        if start.y - 1 >= 0:
            n = Coord(start.x, start.y - 1)
            if not self.close.has_key(n) and not self.open_dict.has_key(n):
                neighbors.append(n)

        if start.y + 1 < max_size:
            n = Coord(start.x, start.y + 1)
            if not self.close.has_key(n) and not self.open_dict.has_key(n):
                neighbors.append(n)

        if start.x + 1 < max_size:
            n = Coord(start.x + 1, start.y)
            if not self.close.has_key(n) and not self.open_dict.has_key(n):
                neighbors.append(n)

        return neighbors

class PathFinderBackwards:
    def __init__(self, maze_file):
        self.close = dict()
        self.open = MinHeap()
        self.open_dict = dict()
        self.grid = []
        self.start_state = None
        self.goal_state = None
        for i in range(max_size):
            self.grid.append([])
        with open(maze_file, 'r') as f:
            line_row = 0
            for line in f:
                self.grid.append([])
                line = line.rstrip()
                if not line:
                    continue
                if not self.start_state:
                    self.start_state = line_to_coord(line)
                    continue
                if not self.goal_state:
                    self.goal_state = line_to_coord(line)
                    self.goal_state.g = 0
                    continue
                for pos in line:
                    self.grid[line_row].append(True if pos == '1' else False)
                line_row += 1

    def find_path(self):
        return self.find_path_internal(self.goal_state, self.start_state, [])


    def find_path_internal(self, start, goal, path):
        path.append(start)
        if start == goal:
            return path
        self.close[start] = True
        neighbors = self.compute_valid_neighbors(start)
        if neighbors:
            for n in neighbors:
                n.g = start.g + 1
                if self.grid[n.y][n.x]:
                    continue
                n.distance = calculate_manhattan_distance(n, goal)
                self.open.insert(n)
                self.open_dict[n] = True
        nextC = self.open.extract()
        if not nextC:
            return []
        return self.find_path_internal(nextC, goal, path)


    def compute_valid_neighbors(self, start):
        neighbors = []
        # Find all neighbors.
        if start.x - 1 >= 0:
            n = Coord(start.x - 1, start.y)
            if not self.close.has_key(n):
                neighbors.append(n)

        if start.y - 1 >= 0:
            n = Coord(start.x, start.y - 1)
            if not self.close.has_key(n) and not self.open_dict.has_key(n):
                neighbors.append(n)

        if start.y + 1 < max_size:
            n = Coord(start.x, start.y + 1)
            if not self.close.has_key(n) and not self.open_dict.has_key(n):
                neighbors.append(n)

        if start.x + 1 < max_size:
            n = Coord(start.x + 1, start.y)
            if not self.close.has_key(n) and not self.open_dict.has_key(n):
                neighbors.append(n)

        return neighbors

class PathFinderTieBreak:
    def __init__(self, maze_file):
        self.close = dict()
        self.open = MinHeap()
        self.open_dict = dict()
        self.grid = []
        self.start_state = None
        self.goal_state = None
        for i in range(max_size):
            self.grid.append([])
        with open(maze_file, 'r') as f:
            line_row = 0
            for line in f:
                self.grid.append([])
                line = line.rstrip()
                if not line:
                    continue
                if not self.start_state:
                    self.start_state = line_to_high_coord(line)
                    self.start_state.g = 0
                    continue
                if not self.goal_state:
                    self.goal_state = line_to_high_coord(line)
                    continue
                for pos in line:
                    self.grid[line_row].append(True if pos == '1' else False)
                line_row += 1

    def find_path(self):
        return self.find_path_internal(self.start_state, self.goal_state, [])


    def find_path_internal(self, start, goal, path):
        path.append(start)
        if start == goal:
            return path
        self.close[start] = True
        neighbors = self.compute_valid_neighbors(start)
        if neighbors:
            for n in neighbors:
                n.g = start.g + 1
                if self.grid[n.y][n.x]:
                    continue
                n.distance = calculate_manhattan_distance(n, goal)
                self.open.insert(n)
                self.open_dict[n] = True
        nextC = self.open.extract()
        if not nextC:
            return []
        return self.find_path_internal(nextC, goal, path)


    def compute_valid_neighbors(self, start):
        neighbors = []
        # Find all neighbors.
        if start.x - 1 >= 0:
            n = HighCoord(start.x - 1, start.y)
            if not self.close.has_key(n):
                neighbors.append(n)

        if start.y - 1 >= 0:
            n = HighCoord(start.x, start.y - 1)
            if not self.close.has_key(n) and not self.open_dict.has_key(n):
                neighbors.append(n)

        if start.y + 1 < max_size:
            n = HighCoord(start.x, start.y + 1)
            if not self.close.has_key(n) and not self.open_dict.has_key(n):
                neighbors.append(n)

        if start.x + 1 < max_size:
            n = HighCoord(start.x + 1, start.y)
            if not self.close.has_key(n) and not self.open_dict.has_key(n):
                neighbors.append(n)

        return neighbors

def calculate_manhattan_distance(start, end):
    return abs(start.x - end.x) + abs(start.y - end.y)

def line_to_coord(line):
    val = [int(x) for x in line.split(",")]
    if len(val) != 2:
        raise ValueError
    return Coord(val[0], val[1])

def line_to_high_coord(line):
    val = [int(x) for x in line.split(",")]
    if len(val) != 2:
        raise ValueError
    return HighCoord(val[0], val[1])

def main():
    sys.setrecursionlimit(10300)
    pf = None
    if sys.argv[1] == "normal":
        pf = PathFinderNormal(sys.argv[2])
    elif sys.argv[1] == "backwards":
        pf = PathFinderBackwards(sys.argv[2])
    elif sys.argv[1] == "tiebreak":
        pf = PathFinderTieBreak(sys.argv[2])
    else:
        print "Bad args. path_finder.py <normal/backwards/tiebreak> <filename>"
        return
    path = pf.find_path()
    print path

if __name__ == '__main__':
    main()
