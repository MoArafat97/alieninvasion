class Ship:
    """This is a ship class"""

    def __int__(self, ai_game):
        """Initialise the ship and it's starting position"""
        self.screen = ai_game
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get it's rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom corner of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)