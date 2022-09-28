# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:33:49 2022

@author: Administrateur
"""

import pygame # importation de la librairie pygame
import space
import sys # pour fermer correctement l'application

# lancement des modules inclus dans pygame
pygame.init() 

# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders") 
# chargement de l'image de fond
fond = pygame.image.load('background.png')
fond = pygame.transform.scale(fond, (800, 60))
# creation du joueur
player = space.Joueur()
# creation de la balle
tir = space.Balle(player)
tir.etat = "chargee"
# creation des ennemis
listeEnnemis = []
for indice in range(space.Ennemi.NbEnnemis):
    vaisseau = space.Ennemi()
    listeEnnemis.append(vaisseau)
    
# Création du texte pour afficher le score et les points de vie du boss
font = pygame.font.Font('freesansbold.ttf', 32)
fontLP = pygame.font.Font('freesansbold.ttf', 20)
    
### BOUCLE DE JEU  ###
running = True # variable pour laisser la fenêtre ouverte
while running : # boucle infinie pour laisser la fenêtre ouverte
    # dessin du fond
    screen.blit(fond,(0,0))
    if player.score >= 2000:
        running = False 
        print(" You WON !!!")
        
    # Affichage du score
    textScore = font.render("Score : " + str(player.score), True, (255,255,255))
    screen.blit(textScore, (600, 10))
    # Affichage des PV du joueur
    text_LP_Player = fontLP.render("LP restants : " + str(player.vie), True, (0,255,0))
    screen.blit(text_LP_Player, (10, 575))
    
    ### Gestion des événements  ###
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            running = False # running est sur False
            sys.exit() # pour fermer correctement
       
       # gestion du clavier
        if event.type == pygame.KEYDOWN : # si une touche a été tapée KEYUP quand on relache la touche
            if event.key == pygame.K_LEFT : # si la touche est la fleche gauche
                player.sens = "gauche" # on déplace le vaisseau de 1 pixel sur la gauche
            if event.key == pygame.K_RIGHT : # si la touche est la fleche droite
                player.sens = "droite" # on déplace le vaisseau de 1 pixel sur la gauche
            if event.key == pygame.K_SPACE : # espace pour tirer
                player.tirer()
                tir.etat = "tiree"

    ### Actualisation de la scene ###
    # Gestions des collisions
    for ennemi in listeEnnemis:
        if tir.toucher(ennemi):
            ennemi.disparaitre()
            player.marquer()
    print(f"Score = {player.score} points")
    # placement des objets
    # le joueur
    player.deplacer()
    screen.blit(tir.image,[tir.depart,tir.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur        
    # la balle
    tir.bouger()
    screen.blit(player.image,[player.position,500]) # appel de la fonction qui dessine le vaisseau du joueur
    # les ennemis
    for ennemi inlisteEnnemis:
        ennemi.avancer()
        # Inflige des dégats au joueur lorsqu'il est touché
        if ennemi.degats(player):
            player.losePV()
            ennemi.disparaitre()
        screen.blit(ennemi.image,[ennemi.depart, ennemi.hauteur]) # appel de la fonction qui dessine les ennemis
        if ennemi.hauteur > 600 : # fait disparaitre l'ennemi s'il sort de l'ecran
            ennemi.disparaitre()
    
        
    
    pygame.display.update() # pour ajouter tout changement à l'écran
