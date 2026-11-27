import pygame
from alien import Alien
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class AlienFleet:

    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed
        self.create_fleet()

    
    def create_fleet(self) -> None:
        """Create a V-shaped alien fleet for Milestone 2."""

        self.fleet.empty()

        center_x = self.settings.screen_w // 2
        start_y = 90

        x_spacing = self.settings.alien_w * 2
        y_spacing = self.settings.alien_h * 2

        rows = 6

        for row in range(rows):
            current_y = start_y + row * y_spacing

            if row == 0:
                self._create_alien(
                    center_x - self.settings.alien_w // 2,
                    current_y
                )
            else:
                left_x = center_x - row * x_spacing
                right_x = center_x + row * x_spacing

                self._create_alien(
                    left_x - self.settings.alien_w // 2,
                    current_y
                )

                self._create_alien(
                    right_x - self.settings.alien_w // 2,
                    current_y
                )

    def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        for row in range(fleet_h):
         for col in range(fleet_w):
            current_x = alien_w * col + x_offset
            current_y = alien_h * row + y_offset
            if col % 2 == 0 or row % 2 == 0:
                continue 
            self._create_alien(current_x, current_y)

    def calculate_offset(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        half_screen = self.settings.screen_h // 2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = int((screen_w - fleet_horizontal_space) // 2)
        y_offset = int((half_screen - fleet_vertical_space) // 2)
        return x_offset,y_offset

    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h ) -> tuple:
        fleet_w = (screen_w // alien_w)
        fleet_h = ((screen_h/2)// alien_h)
        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2
        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2

        return int(fleet_w), int(fleet_h)

    def _create_alien(self, current_x: int, current_y: int) -> None:
      new_alien = Alien(self, current_x, current_y)
      
      self.fleet.add(new_alien)

    def _check_fleet_edges(self) :
       alien : Alien
       for alien in self.fleet:
          if alien.check_edges():
             self._drop_alien_fleet()
             self.fleet_direction *= -1
             break

    def _drop_alien_fleet(self) -> None:
       for alien in self.fleet:
        alien.y += self.fleet_drop_speed
       
    def update_fleet(self) -> None:
        self._check_fleet_edges()
        self.fleet.update()
    def draw(self) -> None:
     alien: 'Alien'
     for alien in self.fleet:
        alien.draw_alien()
    def check_collisions(self, other_group) :
     return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
    # check collisions for aliens and bottom of screen
    def check_fleet_bottom(self) -> bool:
     alien: Alien
     for alien in self.fleet:
        if alien.rect.bottom >= self.settings.screen_h:
            return True

     return False
    def check_destroyed_status(self) :
     return not self.fleet
    