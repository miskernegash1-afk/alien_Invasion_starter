"""
Program Name: Frozen Planet Defense - Track 2
Author: Misker Negash
Purpose: Create and control custom laser projectiles.
Starter Code Links: https://github.com/RedBeard41/alien_Invasion_starter
Date Updated: November 21, 2026
"""


import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Bullet(Sprite):
    """Represent a laser fired from the player's spaceship."""
    def __init__(self, game: 'AlienInvasion') -> None:
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.bullet_w, self.settings.bullet_h)
)



        self.rect = self.image.get_rect()
        self.rect.midbottom = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self) -> None:
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self) -> None:
        self.screen.blit(self.image, self.rect)