"""
Program Name: Frozen Planet Defense - Track 2
Author: Misker Negash
Purpose: Store game settings and custom asset file paths.
Starter Code Links: Add your actual course starter-code URL.
Date Updated: November 21, 2026
"""
from pathlib import Path

class Settings:
    """Store configuration settings for Frozen Planet Defense."""
    def __init__(self) -> None:
         
        """Initialize the game settings and asset paths."""
        self.base_dir = Path(__file__).resolve().parent
        self.name: str = 'Frozen Planet Defense - Track 2'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = self.base_dir / 'Assets' / 'images' / 'frozen_background.png'
        
        self.difficulty_scale = 1.1
        self.scores_file = self.base_dir / 'Assets' / 'file' / 'scores.json'
        
        self.ship_file = self.base_dir / 'Assets' / 'images' / 'frozen_ship.png'
        self.ship_w = 100
        self.ship_h = 140
        

        self.bullet_file = self.base_dir / 'Assets' / 'images' / 'ice_laser.png'
        self.laser_sound = self.base_dir / 'Assets' / 'sound' / 'explosion5.OGG'
        self.impact_sound = self.base_dir / 'Assets' / 'sound' / 'explosion5.OGG'

        
    
        
        self.alien_file = self.base_dir / 'Assets' / 'images' / "frozen_enemy.png"
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 2
        self.fleet_direction = 1
        self.fleet_drop_speed = 40

        self.button_w = 25
        self.button_h = 50
        self.button_color = (0, 135, 50)

        self.text_color = (255, 255, 255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = self.base_dir / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'
        
    def initialize_dynamic_settings(self) -> None:
        self.ship_speed = 5
        self.starting_ship_count = 3
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_speed = 7
        self.bullet_amount = 5
        self.fleet_drop_speed = 40
        self.alien_points = 50


    
    def increase_difficulty(self) -> None:
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale
