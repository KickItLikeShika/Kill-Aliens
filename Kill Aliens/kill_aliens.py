import pygame
from Settings import Settings
from Ship import Ship
import game_functions as gf
from pygame.sprite import Group
from Alien import Alien
from Game_stats import GameStats
from Button import Button
from Score_board import Scoreboard

def run_game():
    """Running the game window."""
    # Intializing the game and create the screen ojbect
    pygame.init()
    # Making instance form the Settings class
    ai_settings = Settings()
    # Set the height and the width of the window
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # Sound settings
    music = pygame.mixer.music.load('music/background_music.mp3')
    pygame.mixer.music.play(-1)
    bullet_sound = pygame.mixer.Sound('music/bullets_sound.wav')
    # Create an instance form GameStats and Scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # Make a ship
    ship = Ship(ai_settings, screen)
    # Make a alien
    alien = Alien(ai_settings, screen)
    # Make a group of bullets and alien
    bullets = Group()
    aliens = Group()
    # Create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Namming the window
    pygame.display.set_caption("Kill Aliens")
    # Change the window icon
    icon = pygame.image.load('images/sss.png')
    pygame.display.set_icon(icon)
    # Draw the play button
    play_button = Button(ai_settings, screen, "Play")
    # Looping to keep the game running
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, bullet_sound)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
