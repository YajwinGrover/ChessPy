import sys
import pygame
from pygame.locals import *

class Pawn(pygame.sprite.Sprite):
    x = 0
    y = 0
    oldX = 0
    oldY = 0
    color = ""
    shouldFollow = False
    firstMove = True
    id = ''

    def __init__(self,newX,newY,ncolor, board):

        super().__init__()
        self.x = newX
        self.y = newY
        self.oldY = newY
        self.oldX = newX
        self.color = ncolor


        self.board = board


        if self.color == 'white':
            self.image = pygame.image.load("ChessKingSacrafice/whitePawn.png")
            self.id = 'P'
        else:
            self.image = pygame.image.load("ChessKingSacrafice/blackPawn.png")
            self.id = 'p'

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def update(self, newX, newY):
        if self.shouldFollow:
            self.rect.center = (newX, newY)
            self.x = newX
            self.y = newY

    def snap(self,boxSize):
        newX = boxSize * (self.x//boxSize)
        newY = boxSize * (self.y//boxSize)
        self.rect.topleft = (newX, newY)
        self.x = newX
        self.y = newY

    def checkMove(self, boxSize):
        if self.firstMove:
            if self.color == 'black':
                distMove = self.y - self.oldY
                if (distMove == boxSize * 2 or distMove == boxSize) and self.x == self.oldX:
                    self.board.remove_piece(self.oldX, self.oldY)
                    self.firstMove = False
                    self.oldX = self.x
                    self.oldY = self.y
                    self.board.set_piece(self.x, self.y, self.id)

                else:
                    self.rect.topleft = (self.oldX, self.oldY)
                    self.x = self.oldX
                    self.y = self.oldY

            elif self.color == 'white':
                distMove = self.oldY - self.y
                if (distMove == boxSize * 2 or distMove == boxSize) and self.x == self.oldX:
                    self.board.remove_piece(self.oldX, self.oldY)
                    self.firstMove = False
                    self.oldX = self.x
                    self.oldY = self.y
                    self.board.set_piece(self.x, self.y, self.id)

                else:
                    self.rect.topleft = (self.oldX, self.oldY)
                    self.x = self.oldX
                    self.y = self.oldY
        else:

            if self.color == 'black':
                distMove = self.y - self.oldY
                if distMove == boxSize and self.x == self.oldX:
                    self.board.remove_piece(self.oldX, self.oldY)
                    self.firstMove = False
                    self.oldX = self.x
                    self.oldY = self.y
                    self.board.set_piece(self.x, self.y, self.id)

                else:
                    self.rect.topleft = (self.oldX, self.oldY)
                    self.x = self.oldX
                    self.y = self.oldY
            elif self.color == 'white':
                distMove = self.oldY - self.y
                if distMove == boxSize and self.x == self.oldX:
                    self.board.remove_piece(self.oldX, self.oldY)
                    self.firstMove = False
                    self.oldX = self.x
                    self.oldY = self.y
                    self.board.set_piece(self.x, self.y, self.id)

                else:
                    self.rect.topleft = (self.oldX, self.oldY)
                    self.x = self.oldX
                    self.y = self.oldY


    def setFollow(self,follow):
        self.shouldFollow = follow

    def draw(self, surface):
        surface.blit(self.image, self.rect)

