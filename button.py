# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 22:15:12 2026

@author: anwar
"""

import pygame.font

class Button:
    
    def __init__(self, ai_game, msg):
         """Initialiser les attributs du bouton."""
         self.screen = ai_game.screen
         self.screen_rect = self.screen.get_rect()
         
         # Définir les dimensions et les propriétés du bouton.
         self.width, self.height = 200, 50
         self.button_color = (0, 255, 0)
         self.text_color = (255, 255, 255)
         self.font = pygame.font.SysFont(None, 48)
         
         # Créer l'objet rect du bouton et le centrer.
         self.rect = pygame.Rect(0, 0, self.width, self.height)
         self.rect.center =  self.screen_rect.center
         
         # Message du bouton créer une fois pour toutes.
         self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """
        Trnsformer msg en une image et centrer le texte dans
        le bouton. """
        self.msg_image = self.font.render(msg, True, 
                                          self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        # Dessiner le bouton vide, puis dessiner le message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        