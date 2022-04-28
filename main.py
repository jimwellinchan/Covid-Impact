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

