"""
Program Name: Frozen Planet Defense - Track 2
Author: Misker Negash
Purpose: Manage laser firing and remove off-screen projectiles.
Starter Code Links: Add the actual course starter-code URL.
Date Updated: November 21, 2026
"""
import pygame
from typing import TYPE_CHECKING
from bullet import Bullet
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Arsenal:
    """Manage the lasers fired by the player's spaceship."""
    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self) -> bool:
        """Update lasers and remove off-screen lasers."""
        self.arsenal.update()
        self._remove_bullets_offscreen()
    
    def _remove_bullets_offscreen(self) -> None:
     for bullet in self.arsenal.copy():
        if bullet.rect.bottom <= 0:
            self.arsenal.remove(bullet)
    
    def draw(self) -> None:
        for bullet in self.arsenal:
            bullet.draw_bullet()
            

    def fire_bullet(self) -> None:
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False