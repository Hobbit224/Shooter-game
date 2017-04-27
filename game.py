import pygame
from player import Player
from game_functions import check_events
# Core game functionality/loop
from enemy import Enemy
# Get group collide and group from sprite module
from pygame.sprite import Group, groupcollide
from bullet import Bullet

def run_game():
	# Initialize all pygame stuff 
	pygame.init()
	# Set up tuple for screen size
	screen_size = (1000,800)
	# Set up a tuple for the bg color
	background_color = (82,135,53)

	# Create pygame screen to use
	screen = pygame.display.set_mode(screen_size)
	# Set a caption on the terminal window
	pygame.display.set_caption("Mars Defender")



	the_player = Player(screen, 100,100)
	bad_guy = Enemy(screen)
	the_player_group = Group()
	the_player_group.add(the_player)
	enemies = Group()
	enemies.add(bad_guy)
	bullets = Group()


	# Main game loop
	while 1:
		screen.fill(background_color)
		
		check_events(the_player, screen, bullets)

		# Draw the player
		for player in the_player_group:
			the_player.draw_me()

		# Draw and update the bad guy
		bad_guy.update_me(the_player)
		bad_guy.draw_me()

		# update and draw the bullets
		for bullet in bullets:
			bullet.update()
			bullet.draw_bullet()

		# Check for collisions
		hero_died = groupcollide(the_player_group, enemies, True, False)







		pygame.display.flip()

run_game()