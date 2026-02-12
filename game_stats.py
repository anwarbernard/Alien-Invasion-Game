# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 20:50:03 2026

@author: anwar
"""

class GameStats :
    """Suivre les statistiques d'Alien Invasion."""
    
    def __init__(self, ai_game):
        """Initialiser les statistiques."""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # Démarrer Alien Invasion dans un état inactif
        self.game_active = False
        
        # Ne jamais réinitialiser le meilleur score.
        self.high_score = 0
        
    def reset_stats(self):
        """
        Initialiser les statistiques qui peuvent changer
        pendant le jeu.
        """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1