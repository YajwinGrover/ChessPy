import sys
import pygame
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((1000,1000*9/16))
pygame.draw.circle(window,'WHITE',(200,50),30 )
FPS = pygame.time.Clock()
FPS.tick(60)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("AvatarMaker copy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)

    def update(self):
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[K_w]:
            self.rect.move_ip(0,-5)
        if pressedKeys[K_s]:
            self.rect.move_ip(0,5)
    def draw(self,surface):
        surface.blit(self.image,self.rect)

P1 = Player()
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P1.update()
    window.fill('WHITE')
    P1.draw(window)
    pygame.display.update()
    FPS.tick(60)

