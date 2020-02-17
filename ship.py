import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""Statek gracza."""
	def __init__(self, ai_settings, screen):
		"""Inicjalizacja statku kosmicznego i jego położenie początkowe."""
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		#Wczytanie obrazu statku kosmicznego i pobranie jego prostokąta.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect() #statek jako kwadrat
		self.screen_rect = screen.get_rect()
		
		#Każdy nowy statek kosmiczny pojawia się na dole ekranu.
		
		###najpierw laduje obrazek, pozniej tworze kwadrat z obrazka, kwadrat z ekranu, pozniej przypisuje kwadrowi obrazka (statku)
		###wartosc srodkowa kwadrata ekranu, a dalej wartosc obrazka wartosc dolna ekranu
		
		#Statek na dole i na srodku
		self.rect.centerx = self.screen_rect.centerx #statek jako kwadrat na srodku ekranu (center, centerx i centery)
		self.rect.bottom = self.screen_rect.bottom #statek jako kwadrat na dole ekranu (bottop, left, right, top ekranu)
		
		#Punkt środkowy jest przechowywany w postaci liczby zmiennoprzecinkowej.
		self.center = float(self.rect.centerx)
		
		#Opcje wsazujące na poruszanie się statku.
		self.moving_right = False
		self.moving_left = False 
	     
	     
	def center_ship(self):
		"""Umieszczenie statsku na środku przy dolnej krawędzi ekranu."""
		self.center = self.screen_rect.centerx
		
		     
	def update(self):
		"""
		Uaktualnienie położenia statku na podstawie opcji wskazującej na jego
		ruch.
		"""
		#Uaktualnienie wartości punktu środkowego statku, a nie jego prostokąta.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
			
		#Uaktualnienie obiektu rect na podstawie wartości self.center.
		self.rect.centerx = self.center 
		
	def blitme(self):
		"""Wyświetlenie statku kosmiczneog w jego aktualnym położeniu."""
		self.screen.blit(self.image, self.rect)
		

	
