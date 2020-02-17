# ~ import sys
import pygame 


from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
# ~ from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
	#Inicjalizacja gry i utworzenie obiektu ekranu.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((
	ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Inwazja obcych")
	
	#Utwozenie przycisku Gra.
	play_button = Button(ai_settings, screen, "Nowa gra")
	
	#Utworzenie egzemplarza przeznaczonego do przechowywania danych
	#statystycznych dotyczących gry oraz utworzenie egzemplarza klasy Scoreboard.
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
	#Utworzenie statku kosmicznego, grupy przeznaczonej do przechywowania pocisków oraz grupy obcych.
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	
	# ~ #Utworzenie obcego
	# ~ alien = Alien(ai_settings, screen)
	
	#Utworzenie floty obcych.
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	#Rozpoczęcie pętli głownej gry.
	while True:
		#Oczekiwanie na naciśnięcie klawisza lub przycisku myszy.
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		if stats.game_active:
			#Odswieżanie ekran w trakcie każdej iteracji pętli.
			#RGB - kolory
			ship.update()		
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
			#Wyświetlenie ostatnio zmodyfikowanego ekranu.
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
		
run_game()
