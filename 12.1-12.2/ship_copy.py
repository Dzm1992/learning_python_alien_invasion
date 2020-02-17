import pygame

class Ship():
	"""Statek gracza."""
	def __init__(self, ai_settings, screen):
		"""Inicjalizacja statku kosmicznego i jego położenie początkowe."""
		self.screen = screen
		self.ai_settings = ai_settings
		
		#Wczytanie obrazu statku kosmicznego i pobranie jego prostokąta.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect() #statek jako kwadrat
		self.screen_rect = screen.get_rect()
		
		#Każdy nowy statek kosmiczny pojawia się na dole ekranu.
		self.rect.centerx = self.screen_rect.centerx #statek jako kwadrat na srodku ekranu (center, centerx i centery)
		self.rect.centery = self.screen_rect.centery #statek jako kwadrat na dole ekranu (bottop, left, right, top ekranu)
		
		###najpierw laduje obrazek, pozniej tworze kwadrat z obrazka, kwadrat z ekranu, pozniej przypisuje kwadrowi obrazka (statku)
		###wartosc srodkowa kwadrata ekranu, a dalej wartosc obrazka wartosc dolna ekranu
		
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
		#Punkt środkowy jest przechowywany w postaci liczby zmiennoprzecinkowej.
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
		#Opcje wsazujące na poruszanie się statku.
		self.moving_right = False
		self.moving_left = False
		self.moving_down = False
		self.moving_up = False
	     
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.centerx -= self.ai_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.centery += self.ai_settings.ship_speed_factor
		if self.moving_up and self.rect.top > 0:
			self.centery -= self.ai_settings.ship_speed_factor
			
		
		if self.moving_up or self.moving_down:
			self.rect.centery = self.centery
		if self.moving_left or self.moving_right:
			self.rect.centerx = self.centerx

		
	def blitme(self):
		"""Wyświetlenie statku kosmiczneog w jego aktualnym położeniu."""
		self.screen.blit(self.image, self.rect)
