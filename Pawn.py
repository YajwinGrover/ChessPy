import sys
import pygame
from pygame.locals import *

class Pawn(pygame.sprite.Sprite):
    x = 0
    y = 0
    color = ""
    shouldFollow = False

    def __init__(self,newX,newY,ncolor):
        super().__init__()
        self.x = newX
        self.y = newY
        color = ncolor
        if(color == 'white'):
            self.image = pygame.image.load("ChessKingSacrafice/whitePawn.png")
        else:
            self.image = pygame.image.load("ChessKingSacrafice/blackPawn.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def update(self, newX, newY):
        if self.shouldFollow:
            self.rect.center = (newX,newY)
            self.x = newX
            self.y = newY

    def snap(self,boxSize):
        newX = boxSize * (self.x//boxSize)
        newY = boxSize * (self.y//boxSize)
        self.rect.topleft = (newX, newY)

    def setFollow(self,follow):
        self.shouldFollow = follow

    def draw(self,surface):
        surface.blit(self.image,self.rect)

