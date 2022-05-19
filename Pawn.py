import sys
import pygame
from pygame.locals import *
from Board import Board
from Piece import Piece

class Pawn(Piece):
    firstMove = True

    def extended_init(self):
        self.id = 'P'
        if self.color == 'white':
            self.image = pygame.image.load("ChessKingSacrafice/whitePawn.png")
        else:
            self.image = pygame.image.load("ChessKingSacrafice/blackPawn.png")
            self.id = 'p'

    def calculate_legal(self):
        self.board.check_pawn(self.x, self.y, self.legal_moves, self.firstMove, self.color)

    def checkMove(self, boxSize):
        self.snap(boxSize)
        if str(self.y//boxSize)+str(self.x//boxSize) in self.legal_moves:
            self.move(boxSize)
            self.oldX = self.x
            self.oldY = self.y
            return True
        return False