import pygame
import sys
from player import Player
from bullet import Bullet



def check_events(the_player, screen, bullets):
	# Escape hatch for while
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			print event.key
			if event.key == 273:
				the_player.should_move("up", True)
			elif event.key == 274:
				the_player.should_move("down", True)
			elif event.key == 275:
				the_player.should_move("right", True)
			elif event.key == 276:
				the_player.should_move("left", True)
			elif event.key == 32:
				# User pressed spacebar, fire!
				for direction in range(1,5):
					new_bullet = Bullet(screen,the_player,direction)
					bullets.add(new_bullet)
			 
		elif event.type == pygame.KEYUP:
			if event.key == 273:
				the_player.should_move("up", False) 
			if event.key == 274:
				the_player.should_move("down", False) 
			if event.key == 276:
				the_player.should_move("left", False) 
			if event.key == 275:
				the_player.should_move("right", False) 






