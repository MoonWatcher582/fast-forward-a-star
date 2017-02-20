import pygame
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

grid_size = 101
block_size = 8
multiplier = 1.13

length = int(math.ceil(multiplier * grid_size * block_size))

size = (length, length)
window = pygame.display.set_mode(size)
pygame.display.set_caption("A* Path")

done = False
clock = pygame.time.Clock()

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	window.fill(BLACK)
	for y in range(grid_size):
		for x in range(grid_size):
			rect = pygame.Rect(x * (block_size + 1), y * (block_size + 1), block_size, block_size)
			pygame.draw.rect(window, WHITE, rect)
	
	pygame.display.flip()
	clock.tick(5)

pygame.quit()
