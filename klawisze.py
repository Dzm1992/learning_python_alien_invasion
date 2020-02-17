import sys

import pygame

def run_game():
    #Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Keys")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
        pygame.display.flip()

run_game()


# The short and simple answer is yes; you're seeing the keycode of each key.

# Pygame is based on SDL, so to see a list of all keycodes take a look at the SDL docs (SDLKeycodeLookup).

# The longer is answer is: it's a little more compliated, since there's also the scancode (SDL_Scancode), which is platform-specific, but you usually don't have to worry about that.

# A more interresting thing to know is that the pygame.KEYDOWN event has a unicode attribute that represents a single character string that is the fully translated character entered.

# https://stackoverflow.com/questions/56470096/expected-output-when-printing-keydown-events-in-pygame
