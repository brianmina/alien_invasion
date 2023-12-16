class Settings:
    """A class to store all setting for ALien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (30, 30, 30)
        self.ship_speed = 1.0

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 50
        self.bullet_height = 60
        self.bullet_color = (255, 97, 3)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 0.05
        self.fleet_drop_speed = 50

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.ship_limit = 3

        # how quickly the game speed up
        self.speedup_scale = 1.1

        # how quickly the alien point values increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game."""
        self.ship_speed = 1.0
        self.bullet_speed = 1
        self.alien_speed = 0.1

        # Fleet direction of 1 representing right; -1 representing left.
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed and alien point value settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

