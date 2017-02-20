import pygame
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

grid_size = 101
block_size = 8
multiplier = 1.13


def run_sim(start_state, end_state, path):
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
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

		window.fill(BLACK)
		for y in range(grid_size):
			for x in range(grid_size):
				rect = pygame.Rect(x * (block_size + 1), y * (block_size + 1), block_size, block_size)
				try:
					curr_path_node_x, curr_path_node_y = path[path_index]
				except IndexError:
					curr_path_node_x, curr_path_node_y = (-1, -1)
				if curr_path_node_x == x and curr_path_node_y == y:
					pygame.draw.rect(window, RED, rect)
				elif start_x == x and start_y == y:
					pygame.draw.rect(window, BLUE, rect)
				elif end_x == x and end_y == y:
					pygame.draw.rect(window, GREEN, rect)
				else:
					pygame.draw.rect(window, WHITE, rect)

		path_index += 1
		pygame.display.flip()
		clock.tick(5)

	pygame.quit()
