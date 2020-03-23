class Settings():
    """A class to store all the settings for the game."""
    
    def __init__(self):
        """Intializing the game statistics."""
        # The screen of the settings
        self.screen_width = 1368
        self.screen_height = 768
        self.bg_color = (30, 30, 50)

        # Ship settings
        self.ship_limit = 1

        # Bullet settings
        self.bullet_width = 4
        self.bullet_height = 20
        self.bullet_color = (255, 255, 255)


        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # How quickly the poing values increase
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """Initialize settings that changes through the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Modify the speed and the score during the game."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)