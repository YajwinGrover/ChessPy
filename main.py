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

# Yes I am sane.
def DESTROYPIECES(term, pieces):
    if not term:
        return
    x = term[1]
    y = term[2]

    for p in pieces:
        if p.x == x and p.y == y and p.id == term[0]:
            pieces.remove(p)


pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
selected = False
boxSize = 90

boardState = "RNBKQBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbkqbnr"
board = Board(boardState, boxSize)

# boardState = "8/1q2P1B1/4P1K1/7N/p2pp3/1bn1p1pk/n7/1B6"

window = pygame.display.set_mode((1280,1280*9/16))
current_turn = "white"
swap_turn = {"white":"black", "black":"white"}

FPS = pygame.time.Clock()
FPS.tick(60)

pieces = []
for i in range(8):
        pieces.append(Pawn(i * boxSize, 6 * boxSize, 'white', board, boxSize))

for i in range(8):
    pieces.append(Pawn(i * boxSize, 1 * boxSize,'black', board, boxSize))


pieces.append(Rook(0 * boxSize,7 * boxSize,'white', board, boxSize))
pieces.append(Knight(1 * boxSize,7 * boxSize,'white', board, boxSize))
pieces.append(Bishob(2 * boxSize,7 * boxSize,'white', board, boxSize))
pieces.append(Queen(3 * boxSize,7 * boxSize,'white', board, boxSize))
pieces.append(King(4 * boxSize,7 * boxSize,'white', board, boxSize))
pieces.append(Bishob(5 * boxSize,7 * boxSize,'white', board, boxSize))
pieces.append(Knight(6 * boxSize,7 * boxSize,'white', board, boxSize))
pieces.append(Rook(7 * boxSize,7 * boxSize,'white', board, boxSize))

pieces.append(Rook(0 * boxSize,0 * boxSize,'black', board, boxSize))
pieces.append(Knight(1 * boxSize,0 * boxSize,'black', board, boxSize))
pieces.append(Bishob(2 * boxSize,0 * boxSize,'black', board, boxSize))
pieces.append(Queen(3 * boxSize,0 * boxSize,'black', board, boxSize))
pieces.append(King(4 * boxSize,0 * boxSize,'black', board, boxSize))
pieces.append(Bishob(5 * boxSize,0 * boxSize,'black', board, boxSize))
pieces.append(Knight(6 * boxSize,0 * boxSize,'black', board, boxSize))
pieces.append(Rook(7 * boxSize,0 * boxSize,'black', board, boxSize))

for i in pieces:
    if i.color == current_turn:
        i.calculate_legal()
    else:
        i.clear_moves()

while True:
    for row in range(0, 8):
        for col in range(0, 8):
            if (row + col) % 2 == 1:
                pygame.draw.rect(window, '#382e12', (boxSize * row, boxSize * col, boxSize, boxSize))

    pygame.draw.rect(window, 'BLACK', (0, 0, 720, 720), 2)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_d:
                for piece in pieces:
                    if piece.shouldFollow and current_turn == piece.color and piece.checkMove(boxSize):
                        piece.move(boxSize)
                        board.print_board()
                        current_turn = swap_turn[current_turn]
                        for i in pieces:
                            if i.color == current_turn:
                                i.calculate_legal()
                            else:
                                i.clear_moves()
                        piece.setFollow(False)
                    elif piece.shouldFollow:
                        piece.setFollow(False)
                        piece.snap_back()
                    else:
                        piece.snap(boxSize)
                DESTROYPIECES(board.get_ded(),pieces)

    pos = pygame.mouse.get_pos()
    for i in pieces:
        i.draw(window)
        i.update(pos[0], pos[1], boxSize)

    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()

        for piece in pieces:
            if piece.rect.collidepoint(pos):
                piece.setFollow(True)
                for i in piece.legal_moves:
                    pygame.draw.rect(window, '#DCDCDC', (boxSize * int(i[1]), int(i[0])*boxSize, boxSize, boxSize))

    pygame.display.update()
    window.fill('#966F33')
    FPS.tick(60)

