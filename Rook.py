import pygame
from pygame.locals import *
from Board import Board
from Piece import Piece

class Rook(Piece):

    def extended_init(self):
        self.id = 'R'
        if self.color == 'white':
            self.image = pygame.image.load("ChessKingSacrafice/whiteRook.png")
        else:
            self.image = pygame.image.load("ChessKingSacrafice/blackRook.png")
            self.id = 'r'

    def calculate_legal(self):
        self.board.check_line(1,0,self.x, self.y, self.legal_moves, self.color)
        self.board.check_line(-1,0,self.x, self.y, self.legal_moves, self.color)
        self.board.check_line(0,1,self.x, self.y, self.legal_moves, self.color)
        self.board.check_line(0,-1,self.x, self.y, self.legal_moves, self.color)

    def checkMove(self, boxSize):
        self.snap(boxSize)
        if str(self.y // boxSize) + str(self.x // boxSize) in self.legal_moves:
            self.move(boxSize)
            self.oldX = self.x
            self.oldY = self.y
            return True
        return False

