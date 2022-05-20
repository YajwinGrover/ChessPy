import sys
import pygame
from pygame.locals import *
from Pawn import Pawn
from Queen import Queen
from King import King
from Rook import Rook
from Knight import Knight
from Bishob import Bishob
from Board import Board
from Save import Save
from time import sleep
# Yes I am sane.
def DESTROYPIECES(term, pieces):
    if not term:
        return
    x = term[1]
    y = term[2]

    for p in pieces:
        if p.x == x and p.y == y and p.id == term[0]:
            pieces.remove(p)

class main():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.my_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.selected = False
        self.boxSize = 90

        self.boardState = "RNBKQBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbkqbnr"
        self.board = Board(self.boardState, self.boxSize)
        self.my_save = Save()

        self.window = pygame.display.set_mode((1280,1280*9/16))
        self.current_turn = "white"
        self.swap_turn = {"white":"black", "black":"white"}

        self.FPS = pygame.time.Clock()
        self.FPS.tick(60)

        self.pieces = []
        self.draw = []
        for i in range(8):
                self.pieces.append(Pawn(i * self.boxSize, 6 * self.boxSize, 'white', self.board, self.boxSize))

        for i in range(8):
            self.pieces.append(Pawn(i * self.boxSize, 1 * self.boxSize,'black', self.board, self.boxSize))


        self.pieces.append(Rook(0 * self.boxSize,7 * self.boxSize,'white', self.board, self.boxSize))
        self.pieces.append(Knight(1 * self.boxSize,7 * self.boxSize,'white', self.board, self.boxSize))
        self.pieces.append(Bishob(2 * self.boxSize,7 * self.boxSize,'white', self.board, self.boxSize))
        self.pieces.append(Queen(3 * self.boxSize,7 * self.boxSize,'white', self.board, self.boxSize))
        self.pieces.append(King(4 * self.boxSize,7 * self.boxSize,'white', self.board, self.boxSize))
        self.pieces.append(Bishob(5 * self.boxSize,7 * self.boxSize,'white', self.board, self.boxSize))
        self.pieces.append(Knight(6 * self.boxSize,7 * self.boxSize,'white', self.board, self.boxSize))
        self.pieces.append(Rook(7 * self.boxSize,7 * self.boxSize,'white', self.board, self.boxSize))

        self.pieces.append(Rook(0 * self.boxSize,0 * self.boxSize,'black', self.board, self.boxSize))
        self.pieces.append(Knight(1 * self.boxSize,0 * self.boxSize,'black', self.board, self.boxSize))
        self.pieces.append(Bishob(2 * self.boxSize,0 * self.boxSize,'black', self.board, self.boxSize))
        self.pieces.append(Queen(3 * self.boxSize,0 * self.boxSize,'black', self.board, self.boxSize))
        self.pieces.append(King(4 * self.boxSize,0 * self.boxSize,'black', self.board, self.boxSize))
        self.pieces.append(Bishob(5 * self.boxSize,0 * self.boxSize,'black', self.board, self.boxSize))
        self.pieces.append(Knight(6 * self.boxSize,0 * self.boxSize,'black', self.board, self.boxSize))
        self.pieces.append(Rook(7 * self.boxSize,0 * self.boxSize,'black', self.board, self.boxSize))
        pygame.display.set_caption("Chess is Cool")

        for i in self.pieces:
            if i.color == self.current_turn:
                i.calculate_legal()
            else:
                i.clear_moves()

        #Save button
        self.save = pygame.font.Font('freesansbold.ttf', 32).render("Save", True, (0, 255, 0), (0, 0, 0))
        self.save_button = self.save.get_rect(topleft=(1000, 0))

        self.read = pygame.font.Font('freesansbold.ttf', 32).render("Read", True, (0, 255, 0), (0, 0, 0))
        self.read_button = self.save.get_rect(topleft=(1000, 50))

    def run(self):
        while True:
            for row in range(0, 8):
                for col in range(0, 8):
                    if (row + col) % 2 == 1:
                        pygame.draw.rect(self.window, '#382e12', (self.boxSize * row, self.boxSize * col, self.boxSize, self.boxSize))

            for i in self.draw:
                pygame.draw.circle(self.window, self.current_turn.upper(), [self.boxSize * int(i[1]) + self.boxSize // 2, int(i[0])*self.boxSize + self.boxSize // 2], 25)

            pygame.draw.rect(self.window, 'BLACK', (0, 0, 720, 720), 2)

            self.window.blit(self.save, self.save_button)
            self.window.blit(self.read, self.read_button)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_d:
                        self.draw = []
                        for piece in self.pieces:
                            if piece.shouldFollow and self.current_turn == piece.color and piece.checkMove(self.boxSize, self.pieces, self.my_save):
                                self.current_turn = self.swap_turn[self.current_turn]
                                for i in self.pieces:
                                    if i.color == self.current_turn:
                                        i.calculate_legal()
                                    else:
                                        i.clear_moves()
                                piece.setFollow(False)
                            elif piece.shouldFollow:
                                piece.setFollow(False)
                                piece.snap_back()
                            else:
                                piece.snap(self.boxSize)
                        DESTROYPIECES(self.board.get_ded(),self.pieces)

            pos = pygame.mouse.get_pos()
            for i in self.pieces:
                i.draw(self.window)
                i.update(pos[0], pos[1], self.boxSize)

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()

                if self.save_button.collidepoint(pos) and self.my_save.save != []:
                    self.my_save.write()

                if self.read_button.collidepoint(pos):
                    self.my_save.read()
                    self.save_run()

                for piece in self.pieces:
                    if piece.rect.collidepoint(pos):
                        piece.setFollow(True)
                        self.draw = piece.legal_moves

            pygame.display.update()
            self.window.fill('#966F33')
            self.FPS.tick(60)

    def save_run(self):
        self.pieces = []

        for i in range(8):
                self.pieces.append(Pawn(i * self.boxSize, 6 * self.boxSize, 'white', self.board, self.boxSize))

        for i in range(8):
            self.pieces.append(Pawn(i * self.boxSize, 1 * self.boxSize,'black', self.board, self.boxSize))


        self.pieces.append(Rook(0 * self.boxSize,7 * self.boxSize,'white', self.board, self.boxSize))
        self.pieces.append(Knight(1 * self.boxSize,7 * self.boxSize,'white', self.board, self.boxSize))
        self.pieces.append(Bishob(2 * self.boxSize,7 * self.boxSize,'white', self.board, self.boxSize))
        self.pieces.append(Queen(3 * self.boxSize,7 * self.boxSize,'white', self.board, self.boxSize))
        self.pieces.append(King(4 * self.boxSize,7 * self.boxSize,'white', self.board, self.boxSize))
        self.pieces.append(Bishob(5 * self.boxSize,7 * self.boxSize,'white', self.board, self.boxSize))
        self.pieces.append(Knight(6 * self.boxSize,7 * self.boxSize,'white', self.board, self.boxSize))
        self.pieces.append(Rook(7 * self.boxSize,7 * self.boxSize,'white', self.board, self.boxSize))

        self.pieces.append(Rook(0 * self.boxSize,0 * self.boxSize,'black', self.board, self.boxSize))
        self.pieces.append(Knight(1 * self.boxSize,0 * self.boxSize,'black', self.board, self.boxSize))
        self.pieces.append(Bishob(2 * self.boxSize,0 * self.boxSize,'black', self.board, self.boxSize))
        self.pieces.append(Queen(3 * self.boxSize,0 * self.boxSize,'black', self.board, self.boxSize))
        self.pieces.append(King(4 * self.boxSize,0 * self.boxSize,'black', self.board, self.boxSize))
        self.pieces.append(Bishob(5 * self.boxSize,0 * self.boxSize,'black', self.board, self.boxSize))
        self.pieces.append(Knight(6 * self.boxSize,0 * self.boxSize,'black', self.board, self.boxSize))
        self.pieces.append(Rook(7 * self.boxSize,0 * self.boxSize,'black', self.board, self.boxSize))

        save_count = 0
        while save_count < len(self.my_save.save):
            for row in range(0, 8):
                for col in range(0, 8):
                    if (row + col) % 2 == 1:
                        pygame.draw.rect(self.window, '#382e12',
                                         (self.boxSize * row, self.boxSize * col, self.boxSize, self.boxSize))

            pygame.draw.rect(self.window, 'BLACK', (0, 0, 720, 720), 2)

            self.window.blit(self.save, self.save_button)
            self.window.blit(self.read, self.read_button)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()


            i = self.my_save.save[save_count]
            for j in self.pieces:
                if j.x == int(i[0])*self.boxSize and j.y == int(i[1])*self.boxSize:
                    self.my_save.move(j, j.x, j.y, int(i[-2])*self.boxSize, int(i[-1])*self.boxSize)
                    j.y = int(i[-1])*self.boxSize
                    j.x = int(i[-2])*self.boxSize
                    j.rect.topleft = (j.x, j.y)
                    sleep(1.0)

            for i in self.pieces:
                i.draw(self.window)

            save_count += 1
            pygame.display.update()
            self.window.fill('#966F33')
            self.FPS.tick(60)


chess = main()
chess.run()