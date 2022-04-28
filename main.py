import pygame
import os
from pygame import mixer
import time
import random
pygame.font.init()
pygame.mixer.init()
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Covid Impact")

shoot_fx = pygame.mixer.Sound('assets/Syringe.mp3')
shoot_fx.set_volume(0.5)

# Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "infected red.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "infected green.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "infected blue.png"))

# Player player
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "nurse.png"))