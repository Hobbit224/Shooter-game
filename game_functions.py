import pygame
import sys

def check_events():
	# Escape hatch for while
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()