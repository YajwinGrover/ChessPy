import pygame
from pygame.locals import *

class King(pygame.sprite.Sprite):
    x = 0
    y = 0
    oldX = 0
    oldY = 0
    shouldFollow = False
    color = ''

    def __init__(self,newX, newY,ncolor, board):
        super().__init__()
        self.x = newX
        self.y = newY
        self.color = ncolor
        self.oldX = newX
        self.oldY = newY
        self.board = board

        if self.color == 'white':
            self.image = pygame.image.load("ChessKingSacrafice/whiteKing.png")
        else:
            self.image = pygame.image.load("ChessKingSacrafice/blackKing.png")

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def update(self, newX, newY):
        if self.shouldFollow:
            self.rect.center = (newX, newY)
            self.x = newX
            self.y = newY

    def snap(self, boxSize):
        newX = boxSize * (self.x // boxSize)
        newY = boxSize * (self.y // boxSize)
        self.rect.topleft = (newX, newY)
        self.x = newX
        self.y = newY

    def checkMove(self, boxSize):
        distX = abs(self.x - self.oldX)
        distY = abs(self.y - self.oldY)
        print(self.x/90, self.y/90)

        if distY <= 90 and distX <= 90 and (self.board.get_piece(int(self.x / 90), int(self.y / 90)).isupper or self.board.get_piece(int(self.x / 90), int(self.y / 90)) == '-'):
                self.board.remove_piece(int(self.oldX/90), int(self.oldY/90))
                self.oldX = self.x
                self.oldY = self.y
                self.board.set_piece(int(self.x/90), int(self.y/90), 'K')
        else:
            self.rect.topleft = (self.oldX, self.oldY)
            self.x = self.oldX
            self.y = self.oldY

    def setFollow(self, follow):
        self.shouldFollow = follow

    def draw(self, surface):
        surface.blit(self.image, self.rect)
