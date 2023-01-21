# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 22:46:03 2023

@author: vansh
"""

import pygame

# Initialize pygame
pygame.init()

# Set the screen size
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("My Game")

# Run the game loop
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # Clear the screen
    screen.fill((255, 255, 255))
    
    # Update the screen
    pygame.display.flip()

# Exit pygame
pygame.quit()

