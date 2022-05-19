import pygame
from pygame.locals import *
from Board import Board
from Piece import Piece

class Knight(Piece):
    def extended_init(self):
        self.id = 'N'
        if self.color == 'white':
            self.image = pygame.image.load("ChessKingSacrafice/whiteKnight.png")
        else:
            self.image = pygame.image.load("ChessKingSacrafice/blackKnight.png")
            self.id = 'n'

    def calculate_legal(self):
        self.board.check_knight(self.x, self.y, self.legal_moves, self.color)

    def checkMove(self, boxSize):
        self.snap(boxSize)
        if str(self.y // boxSize) + str(self.x // boxSize) in self.legal_moves:
            self.move(boxSize)
            self.oldX = self.x
            self.oldY = self.y
            return True
        return False