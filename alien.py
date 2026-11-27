import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet


class Alien(Sprite):
    def __init__(self, fleet:'AlienFleet', x: float, y: float) -> None:
        super().__init__()

        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.alien_w, self.settings.alien_h) 
)



        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self) -> None:
     temp_speed = self.settings.fleet_speed

     #if self.check_edges():
      #  self.settings.fleet_direction *= -1
       # self.y += self.settings.fleet_drop_speed

     self.x += temp_speed * self.fleet.fleet_direction
     self.rect.x = self.x
     self.rect.y = self.y
        
    def check_edges(self) -> bool:
     return ( self.rect.right >= self.boundaries.right or self.rect.left <= self.boundaries.left)

    def draw_alien(self) -> None:
        self.screen.blit(self.image, self.rect)
        self._draw_ice_explosion()

    def _draw_ice_explosion(self) -> None:
        """Draw a pulsing blue explosion below an active alien."""
        phase = (pygame.time.get_ticks() // 150) % 2

        center_x = self.rect.centerx
        center_y = self.rect.bottom + 10

        radius = 5 if phase == 0 else 9
        color = (70, 210, 255)

        # Draw the glowing explosion ring.
        pygame.draw.circle(
            self.screen,
            color,
            (center_x, center_y),
            radius,
            2
        )

        # Draw horizontal energy sparks.
        pygame.draw.line(
            self.screen,
            color,
            (center_x - radius - 5, center_y),
            (center_x + radius + 5, center_y),
            2
        )

        # Draw vertical energy sparks.
        pygame.draw.line(
            self.screen,
            color,
            (center_x, center_y - radius - 5),
            (center_x, center_y + radius + 5),
            2
        )
