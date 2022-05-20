import pygame
from pygame.locals import *
from Board import Board
from Piece import Piece
class Bishob(Piece):

    def extended_init(self):
        self.id = 'B'
        if self.color == 'white':
            self.image = pygame.image.load("ChessKingSacrafice/whiteBishob.png")
        else:
            self.image = pygame.image.load("ChessKingSacrafice/blackBishob.png")
            self.id = 'b'

    def calculate_legal(self):
        self.board.check_line(1, 1, self.x, self.y, self.legal_moves, self.color)
        self.board.check_line(-1, 1, self.x, self.y, self.legal_moves, self.color)
        self.board.check_line(1, -1, self.x, self.y, self.legal_moves, self.color)
        self.board.check_line(-1, -1, self.x, self.y, self.legal_moves, self.color)

