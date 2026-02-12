# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 16:33:34 2026

@author: anwar
"""

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Classe pour représenter un alien."""
    
    def __init__(self, ai_game):
        """
        Initialiser l'alien et définir sa position initiale.
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # Charger l'image d'alien et définir son attribut rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.scale(self.image, (40, 80))
        self.rect = self.image.get_rect()
        
        # Placer chaque nouvel alien près de l'angle supérieur
        # gauche de l'écran
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Stocker la position horizontale exacte de l'alien.
        self.x = float(self.rect.x)
        
    def check_edges(self):
        """Renvoyer True si l'alien est au bord de l'écran."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
            
    def update(self):
        """Déplacer l'alien vers la gauche ou la droite."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x