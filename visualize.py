import pygame
import math
import sys
import re

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

grid_size = 101
block_size = 8
multiplier = 1.13
fps = 60

def run_sim(start_state, end_state, path, maze):
	start_x, start_y = start_state
	end_x, end_y = end_state

	pygame.init()

	length = int(math.ceil(multiplier * grid_size * block_size))

	size = (length, length)
	window = pygame.display.set_mode(size)
	pygame.display.set_caption("A* Path")

	done = False
	clock = pygame.time.Clock()

	path_index = 0
	revealed_path = {}
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

		window.fill(BLACK)
		for y in range(grid_size):
			for x in range(grid_size):
				rect = pygame.Rect(x * (block_size + 1), y * (block_size + 1), block_size, block_size)

				if path_index < len(path):
					curr_path_node_x, curr_path_node_y = path[path_index]
					revealed_path[(curr_path_node_x, curr_path_node_y)] = True
				
				if start_x == x and start_y == y:
					pygame.draw.rect(window, BLUE, rect)
				elif end_x == x and end_y == y:
					pygame.draw.rect(window, GREEN, rect)
				elif revealed_path.get((x, y)):
					pygame.draw.rect(window, RED, rect)
				else:
					if maze[y][x]:
						pygame.draw.rect(window, WHITE, rect)
					else:
						pygame.draw.rect(window, BLACK, rect)

		path_index += 1
		pygame.display.flip()
		clock.tick(fps)

	pygame.quit()

def main():
	start_state = None
	end_state = None
	path = None
	maze = {}

	with open(sys.argv[1], 'r') as f:
		line_row = 0
		for line in f:
			if not line:
				continue
			if not start_state:
				start_state = [int(n) for n in line.split(',')]
				continue
			if not end_state:
				end_state = [int(n) for n in line.split(',')]
				continue
			line_col = 0
			maze[line_row] = {}
			for pos in line:
				maze[line_row][line_col] = True if pos == '0' else False
				line_col += 1
			line_row += 1

	# print start_state
	# print end_state

	with open(sys.argv[2], 'r') as f:
		path_string = f.read()
		path_string_list = re.findall(r'{([0-9]+, [0-9]+)}', path_string)
		path = []
		for pair in path_string_list:
			path.append([int(n) for n in pair.split(',')])

	# print path

	run_sim(start_state, end_state, path, maze)

if __name__ == '__main__':
	main()
