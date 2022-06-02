import pygame
from settings import Settings
from ship import Ship
import functions as f
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run():
    pygame.init()
    ai_settings = Settings()

    """pygame.mouse.set_visible(False)"""

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_width))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(screen, ai_settings)

    # Make a group to store bullets in.
    bullets = pygame.sprite.Group()

    # Make an alien.
    aliens = pygame.sprite.Group()
    # Create the fleet of aliens.
    f.create_fleet(ai_settings, screen, ship, aliens)

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make the Play button.
    play_button = Button(screen, "Play")

    while True:
        f.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            f.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            f.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        f.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run()
