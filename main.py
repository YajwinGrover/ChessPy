import sys
import pygame
from pygame.locals import *

pygame.init()
blackQueen = pygame.image.load('ChessKingSacrafice/blackQueen.png')
window = pygame.display.set_mode((1280,1280*9/16))
window.fill('#966F33')
boxSize = 90
for row in range(0, 8):
    for col in range(0, 8):
        if ((row + col) % 2 == 0):
            pygame.draw.rect(window, '#382e12', (boxSize*row, boxSize*col, boxSize, boxSize))

pygame.draw.rect(window,'BLACK',(0,0,720,720),2)
FPS = pygame.time.Clock()
FPS.tick(60)

# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.image.load("AvatarMaker copy.png")
#         self.rect = self.image.get_rect()
#         self.rect.center = (160,520)
#
#     def update(self):
#         pressedKeys = pygame.key.get_pressed()
#         if pressedKeys[K_w]:
#             self.rect.move_ip(0,-5)
#         if pressedKeys[K_s]:
#             self.rect.move_ip(0,5)
#     def draw(self,surface):
#         surface.blit(self.image,self.rect)
#
# P1 = Player()
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    window.blit(blackQueen,(0,0))
    pygame.display.update()
    FPS.tick(60)

