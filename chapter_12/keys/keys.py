import sys

import pygame

class Keys:

    def __init__(self):
        """Inicializa o jogo e cria recursos"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Keys")

    def run_game(self):
        """Inicia o loop principal do jogo."""
        while True:
            self._check_events() 

    def _check_events(self):
        """Respond to keypress and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)

if __name__ == "__main__":
    # Make a game instance, and run the game

    keys = Keys()
    keys.run_game()