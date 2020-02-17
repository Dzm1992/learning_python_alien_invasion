import sys
import pygame

from settings_copy import Settings
from ship_copy import Ship
import game_functions_copy as gf

def run_game():
	#Inicjalizacja gry i utworzenie obiektu ekranu.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((
	ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Inwazja obcych")
	
	#Utworzenie statku kosmicznego.
	ship = Ship(ai_settings, screen)
	
	#Rozpoczęcie pętli głownej gry.
	while True:
		#Oczekiwanie na naciśnięcie klawisza lub przycisku myszy.
		gf.check_events(ship)	
		#Odswieżanie ekran w trakcie każdej iteracji pętli.
		#RGB - kolory
		ship.update()		
		#Wyświetlenie ostatnio zmodyfikowanego ekranu.
		gf.update_screen(ai_settings, screen, ship)
		
run_game()
