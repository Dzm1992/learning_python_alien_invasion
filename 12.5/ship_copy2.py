import pygame

class Ship():
	"""Statek gracza."""
	def __init__(self, ai_settings, screen):
		"""Inicjalizacja statku kosmicznego i jego położenie początkowe."""
		self.screen = screen
		self.ai_settings = ai_settings
		
		#Wczytanie obrazu statku kosmicznego i pobranie jego prostokąta.
		self.image = pygame.image.load('images/ship_copy2.bmp')
		self.rect = self.image.get_rect() #statek jako kwadrat
		self.screen_rect = screen.get_rect()
		
		#Każdy nowy statek kosmiczny pojawia się na dole ekranu.
		
		###najpierw laduje obrazek, pozniej tworze kwadrat z obrazka, kwadrat z ekranu, pozniej przypisuje kwadrowi obrazka (statku)
		###wartosc srodkowa kwadrata ekranu, a dalej wartosc obrazka wartosc dolna ekranu
		
		#Statek po lewej i na srodku
		self.rect.left = self.screen_rect.left #statek jako kwadrat na srodku ekranu (center, centerx i centery)
		self.rect.centery = self.screen_rect.centery
		
		#Punkt środkowy jest przechowywany w postaci liczby zmiennoprzecinkowej.
		self.center = float(self.rect.centery)
		
		#Opcje wsazujące na poruszanie się statku.
		self.moving_up = False
		self.moving_down = False 
	     
	def update(self):
		"""
		Uaktualnienie położenia statku na podstawie opcji wskazującej na jego
		ruch.
		"""
		#Uaktualnienie wartości punktu środkowego statku, a nie jego prostokąta.
		if self.moving_up and self.rect.top > 0:
			self.center -= self.ai_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.center += self.ai_settings.ship_speed_factor
			
		#Uaktualnienie obiektu rect na podstawie wartości self.center.
		self.rect.centery = self.center 
		
	def blitme(self):
		"""Wyświetlenie statku kosmiczneog w jego aktualnym położeniu."""
		self.screen.blit(self.image, self.rect)
