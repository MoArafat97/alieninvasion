import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """This is the overall class to manage the game assets and behaviour"""

    def __int__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(1200, 900)
        pygame.display.set_caption(" Alien Invasion")

        self.ship = Ship(self)

        # Set a colour
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update the images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
