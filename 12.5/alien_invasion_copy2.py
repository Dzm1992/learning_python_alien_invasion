import sys
import pygame 


from settings_copy2 import Settings
from ship_copy2 import Ship
import game_functions_copy2 as gf
from pygame.sprite import Group

def run_game():
	#Inicjalizacja gry i utworzenie obiektu ekranu.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((
	ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Inwazja obcych")
	
	#Utworzenie statku kosmicznego.
	ship = Ship(ai_settings, screen)
	
	#Utworzenie grupy przeznaczonej do przechywowania pocisków.
	bullets = Group()
	
	#Rozpoczęcie pętli głownej gry.
	while True:
		#Oczekiwanie na naciśnięcie klawisza lub przycisku myszy.
		gf.check_events(ai_settings, screen, ship, bullets)
		#Odswieżanie ekran w trakcie każdej iteracji pętli.
		#RGB - kolory
		ship.update()		
		gf.update_bullets(bullets, ai_settings)
		#Wyświetlenie ostatnio zmodyfikowanego ekranu.
		gf.update_screen(ai_settings, screen, ship, bullets)
		
run_game()
