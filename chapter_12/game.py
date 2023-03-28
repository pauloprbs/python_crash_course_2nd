import sys

import pygame

from settings import Settings
from car import Car

class CarGame:
    """A game with a car."""

    def __init__(self):
        """Inicializa o jogo e cria recursos"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Car Game")

        self.car = Car(self)

    def run_game(self):
        """Inicia o loop principal do jogo."""
        while True:
            self._check_events()
            self._update_screen()   

    def _check_events(self):
        """Respond to keypress and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        """Update images in the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.car.blitme()

        pygame.display.flip()

if __name__ == "__main__":
    # Make a game instance, and run the game

    cg = CarGame()
    cg.run_game()
