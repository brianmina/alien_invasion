class Settings:
    """A class to store all setting for ALien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (30, 30, 30)
        self.ship_speed = 1.5
        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 30
        self.bullet_height = 30
        self.bullet_color = (255, 97, 3)
        self.bullets_allowed = 3
        # Alien settings
        self.alien_speed = 0.1
        self.fleet_drop_speed = 50
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.ship_limit = 3
