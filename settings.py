class Setting:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.text_color = (240, 240, 240)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings

        self.bullet_width = 6
        self.bullet_height = 30
        self.bullet_color = (200, 30, 30)

        # Alien settings

        self.fleet_drop_speed = 15

        # How quickly the game speeds up
        self.speedup_scale = 1.2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Init settings that change during the game."""


        self.ship_speed = 0.8
        self.alien_speed = 0.3
        self.bullet_speed = 1.0
        self.bullets_allowed = 4
        # Scoring
        self.alien_points = 10

        # fleet_direction of 1=right, -1=left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase Alien Speed"""
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.ship_speed *= 1.1
        self.bullets_allowed += 1
