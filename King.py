import pygame
from pygame.locals import *
from Board import Board
from Piece import Piece

class King(Piece):

    def extended_init(self):
        self.id = 'K'
        if self.color == 'white':
            self.image = pygame.image.load("ChessKingSacrafice/whiteKing.png")
        else:
            self.image = pygame.image.load("ChessKingSacrafice/blackKing.png")
            self.id = 'k'

    def calculate_legal(self):
        self.board.check_king(self.x, self.y, self.legal_moves, self.color)

