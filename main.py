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

# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "virus.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "green virus.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "blue virus.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "syringe.png"))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Lab Background.png")), (WIDTH, HEIGHT))

class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

class Ship:
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1