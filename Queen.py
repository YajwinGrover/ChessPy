import pygame
from pygame.locals import *
from Board import Board

class Queen(pygame.sprite.Sprite):
    x = 0
    y = 0
    oldX = 0
    oldY = 0
    shouldFollow = False
    color = ''
    board = None
    id = 1

    def __init__(self,newX, newY,ncolor, board):
        super().__init__()
        self.x = newX
        self.y = newY
        self.color = ncolor
        self.oldX = newX
        self.oldY = newY
        self.board = board

        if self.color == 'white':
            self.image = pygame.image.load("ChessKingSacrafice/whiteQueen.png")
        else:
            self.image = pygame.image.load("ChessKingSacrafice/blackQueen.png")
            id = 7

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
        if self.x == self.oldX or self.y == self.oldY:
            self.board.remove_piece(self.oldX, self.oldY)
            self.oldX = self.x
            self.oldY = self.y
            if self.color == 'black':
                self.board.set_piece(self.x, self.y, 'q')
            else:
                self.board.set_piece(self.x, self.y, 'Q')
        elif distX == distY:
            self.board.remove_piece(self.oldX, self.oldY)
            self.oldX = self.x
            self.oldY = self.y
            if self.color == 'black':
                self.board.set_piece(self.x, self.y, 'q')
            else:
                self.board.set_piece(self.x, self.y, 'Q')
        else:
            self.rect.topleft = (self.oldX, self.oldY)
            self.x = self.oldX
            self.y = self.oldY

    def setFollow(self, follow):
        self.shouldFollow = follow

    def draw(self, surface):
        surface.blit(self.image, self.rect)
