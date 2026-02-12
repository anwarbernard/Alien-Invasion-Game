# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 22:49:57 2026

@author: anwar
"""

class Settings:
    """ Classe pour stocker les paramètres d'Alien Invasion. """
    
    def __init__(self):
        """Initialiser les paramètres statiques du jeu."""
        #Paramètres de l'écran
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (127, 210, 255)
        # Paramètres de la fusée
        self.ship_limit = 3
        # Paramètres des balles
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        # Paramètres des aliens
        self.fleet_drop_speed = 10
        
        # Rythme d'accélération du jeu
        self.speedup_scale = 1.1
        # Rapidité d'augmentation de la valeur en points
        # des aliens
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        Initialiser les paramètres qui changent pendant
        la partie.
        """
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        
        # fleet_direction = 1 correspond à la droite ;
        # -1 à la gauche
        self.fleet_direction = 1
        
        # Score
        self.alien_points = 50
        
    def increase_speed(self):
        """
        Augmenter les paramètres de vitesse et la vaeur 
        en points des aliens.
        """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)