class Coord:
    def __init__(self, x, y):
        self.x=x
        self.y=y

class PathFinder:
    def __init__(self, maze_file):
        self.grid = []
        self.start_state = None
        self.end_state = None
        for i in range(101):
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
                if not self.end_state:
                    self.end_state = line_to_coord(line)
                    continue
                for pos in line:
                    self.grid[line_row].append(True if pos == '1' else False)
                line_row += 1


    def find_path(self, start, goal):
        # TODO: A* here.
        pass

    def calculate_manhattan_distance(self, start, end):
        #TODO: Manhattan distance calucation.
        pass

def line_to_coord(line):
	val = [int(x) for x in line.split(",")]
	if len(val) != 2:
		raise ValueError
	return Coord(val[0], val[1])
