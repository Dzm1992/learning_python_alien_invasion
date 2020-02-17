import sys

import pygame

def check_keydown_events(event, ship):
	"""Responds to keypresses"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_UP:
		ship.moving_up = True
		
		
def check_keyup_events(event, ship):
    """Responds to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False


def check_events(ship):
	"""Reakcja na zdarzenie generowane przez klawiaturę i mysz."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ship)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
			
			
def update_screen(ai_settings, screen, ship):
	"""Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
	#Odświeżenie ekranu w trakcie każdej iteracji pętli.
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	
	#Wyświetlenie ostatnio zmodyfikowanego ekranu.
	pygame.display.flip()
