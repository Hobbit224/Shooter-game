import pygame
from player import Player
from game_functions import check_events
# Core game functionality/loop

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



	the_player = Player(screen)


	# Main game loop
	while 1:
		screen.fill(background_color)
		
		check_events()

		# Draw the player
		the_player.draw_me()



		pygame.display.flip()

run_game()