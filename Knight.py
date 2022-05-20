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