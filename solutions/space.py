# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:27:09 2022

@author: Administrateur
"""

import pygame  # necessaire pour charger les images et les sons
import random
import math

class Joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        self.position = 400
        self.image = pygame.image.load("galaga.png")
        self.images = pygame.transform.scale(self.image, (64, 64))
        self.sens = "O"
        self.vitesse = 2
        self.score = 0
        self.vie = 10

    def deplacer(self) :
        if (self.sens == "droite") and (self.position < 740):
            self.position = self.position + self.vitesse
        elif (self.sens == "gauche") and (self.position > 0):
            self.position = self.position - self.vitesse
           
    def tirer(self):
        self.sens = "O"
        
    def marquer(self):
        self.score = self.score + self.point_gagne
        
    def life_less(self):
        self.vie = self.vie - 1

class Balle() :
    def __init__(self, tireur):
        self.tireur = tireur
        self.depart = tireur.position + 16
        self.hauteur = 492
        self.image = pygame.image.load("balle.png")
        self.etat = "chargee"
        self.vitesse = 5
    
    def bouger(self):
        if self.etat == "chargee":
            self.depart = self.tireur.position + 16
            self.hauteur = 492
        elif self.etat == "tiree" :
            self.hauteur = self.hauteur - self.vitesse
        if self.hauteur < 0:
            self.etat = "chargee"
                
    def toucher(self, vaisseau):
        if (math.fabs(self.hauteur - vaisseau.hauteur) < 40) and (math.fabs(self.depart - vaisseau.depart) < 40):
            self.etat = "chargee"
            return True
  
class Ennemi():
    
    NbEnnemis = random.randint(3, 6)
    
    def __init__(self):
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,2)
        if  (self.type == 1):
            self.image = pygame.image.load("invader1.png")
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.vitesse = 0.5
        elif (self.type ==2):
            self.image = pygame.image.load("bee.png")
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.vitesse = 1
            
    def avancer(self):
        self.hauteur = self.hauteur + self.vitesse
    
    def disparaitre(self):
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,2)
        if  (self.type == 1):
            self.image = pygame.image.load("invader1.png")
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.vitesse = 0.1
            self.point_gagne = 100
        elif (self.type ==2):
            self.image = pygame.image.load("bee.png")
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.vitesse = 0.2
            self.point_gagne = 200
            
    def degats(self, vaisseau):
        if (math.fabs(self.hauteur - vaisseau.hauteur) < 40) and (math.fabs(self.depart - vaisseau.position) < 40):
            return True
