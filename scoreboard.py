import pygame.font
from pygame.sprite import Group


class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information
        self.font = pygame.font.SysFont(None, 36)

        # Prepare the initial score image.
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        hiscore_str = str("Score: " + str(self.stats.hiscore))
        score_str = str("Score: " + str(self.stats.score))
        lives_str = str("Lives: " + str(self.stats.ships_left))

        self.score_image = self.font.render(score_str, True, self.settings.text_color, self.settings.bg_color)
        self.hiscore_image = self.font.render(hiscore_str, True, self.settings.text_color, self.settings.bg_color)
        self.lives_image = self.font.render(lives_str, True, self.settings.text_color, self.settings.bg_color)

        # Display the score at the top left of the screen.

        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 20

        # Display the highscore at the top right of the screen

        self.hiscore_rect = self.hiscore_image.get_rect()
        self.hiscore_rect.right = self.screen_rect.right - 20
        self.hiscore_rect.top = 20

        # Display lives left in the center

        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.centerx = self.screen_rect.centerx
        self.lives_rect.top = 20

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.hiscore_image, self.hiscore_rect)
        self.screen.blit(self.lives_image, self.lives_rect)