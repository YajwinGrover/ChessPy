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

def buildBoardFromString(fen):
    board = [[],[],[],[],[],[],[],[]]
    row = 7
    for char in fen:
        if char != '/':
            if '0' < char < '9':
                for i in range(ord(char)-48):
                    board[row].append('')
            else:
                board[row].append(char)
        else:
            row-= 1
    return board

def charToImg(char):
    #KQRBNPkqrbnp

    if char == 'R':
        return 2
    elif char == 'N':
        return 4
    elif char == 'B':
        return 3
    elif char == 'K':
        return 0
    elif char == 'Q':
        return 1
    elif char == 'P':
        return 5
    elif char == 'r':
        return 8
    elif char == 'n':
        return 10
    elif char == 'b':
        return 9
    elif char == 'k':
        return 6
    elif char == 'q':
        return 7
    elif char == 'p':
        return 11
    else:
        return 0



pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
selected = False

boardState = "RNBKQBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbkqbnr"
board = Board(boardState)

# boardState = "8/1q2P1B1/4P1K1/7N/p2pp3/1bn1p1pk/n7/1B6"
images = []
images.append(pygame.image.load("ChessKingSacrafice/whiteKing.png"))
images.append(pygame.image.load("ChessKingSacrafice/whiteQueen.png"))
images.append(pygame.image.load("ChessKingSacrafice/whiteRook.png"))
images.append(pygame.image.load("ChessKingSacrafice/whiteBishob.png"))
images.append(pygame.image.load("ChessKingSacrafice/whiteKnight.png"))
images.append(pygame.image.load("ChessKingSacrafice/whitePawn.png"))
images.append(pygame.image.load("ChessKingSacrafice/blackKing.png"))
images.append(pygame.image.load("ChessKingSacrafice/blackQueen.png"))
images.append(pygame.image.load("ChessKingSacrafice/blackRook.png"))
images.append(pygame.image.load("ChessKingSacrafice/blackBishob.png"))
images.append(pygame.image.load("ChessKingSacrafice/blackKnight.png"))
images.append(pygame.image.load("ChessKingSacrafice/blackPawn.png"))


window = pygame.display.set_mode((1280,1280*9/16))

boxSize = 90



FPS = pygame.time.Clock()
FPS.tick(60)





pieces = []
for i in range(8):
        pieces.append(Pawn(i * boxSize, 6 * boxSize, 'white', board))

for i in range(8):
    pieces.append(Pawn(i * boxSize, 1 * boxSize,'black', board))


pieces.append(Rook(0 * boxSize,7 * boxSize,'white', board))
pieces.append(Knight(1 * boxSize,7 * boxSize,'white', board))
pieces.append(Bishob(2 * boxSize,7 * boxSize,'white', board))
pieces.append(Queen(3 * boxSize,7 * boxSize,'white', board))
pieces.append(King(4 * boxSize,7 * boxSize,'white', board))
pieces.append(Bishob(5 * boxSize,7 * boxSize,'white', board))
pieces.append(Knight(6 * boxSize,7 * boxSize,'white', board))
pieces.append(Rook(7 * boxSize,7 * boxSize,'white', board))

pieces.append(Rook(0 * boxSize,0 * boxSize,'black', board))
pieces.append(Knight(1 * boxSize,0 * boxSize,'black', board))
pieces.append(Bishob(2 * boxSize,0 * boxSize,'black', board))
pieces.append(Queen(3 * boxSize,0 * boxSize,'black', board))
pieces.append(King(4 * boxSize,0 * boxSize,'black', board))
pieces.append(Bishob(5 * boxSize,0 * boxSize,'black', board))
pieces.append(Knight(6 * boxSize,0 * boxSize,'black', board))
pieces.append(Rook(7 * boxSize,0 * boxSize,'black', board))

while True:
    for row in range(0, 8):
        for col in range(0, 8):
            if ((row + col) % 2 == 1):
                pygame.draw.rect(window, '#382e12', (boxSize * row, boxSize * col, boxSize, boxSize))
    pygame.draw.rect(window, 'BLACK', (0, 0, 720, 720), 2)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_d:
                for piece in pieces:
                    if piece.shouldFollow:
                        piece.setFollow(False)
                        piece.snap(boxSize)
                        piece.checkMove(boxSize)
                    else:
                        piece.setFollow(False)
                        piece.snap(boxSize)

    pos = pygame.mouse.get_pos()
    for i in pieces:
        i.draw(window)
        i.update(pos[0], pos[1])

    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()

        for piece in pieces:
            if piece.rect.collidepoint(pos):
                piece.setFollow(True)

    pygame.display.update()
    window.fill('#966F33')
    FPS.tick(60)

