import sys
import pygame
from pygame.locals import *


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
boardState = "RNBKQBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbkqbnr"
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
window.fill('#966F33')
boxSize = 90
for row in range(0, 8):
    for col in range(0, 8):
        if ((row + col) % 2 == 0):
            pygame.draw.rect(window, '#382e12', (boxSize*row, boxSize*col, boxSize, boxSize))

pygame.draw.rect(window,'BLACK',(0,0,720,720),2)
FPS = pygame.time.Clock()
FPS.tick(60)


# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.image.load("AvatarMaker copy.png")
#         self.rect = self.image.get_rect()
#         self.rect.center = (160,520)
#
#     def update(self):
#         pressedKeys = pygame.key.get_pressed()
#         if pressedKeys[K_w]:
#             self.rect.move_ip(0,-5)
#         if pressedKeys[K_s]:
#             self.rect.move_ip(0,5)
#     def draw(self,surface):
#         surface.blit(self.image,self.rect)
#
# P1 = Player()
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    boardArr = buildBoardFromString(boardState)
    for row in range(len(boardArr)):
        for col in range(len(boardArr[row])):
            if boardArr[row][col] != '':
                window.blit(images[charToImg(boardArr[row][col])], (col * boxSize, row * boxSize))

    pygame.display.update()
    FPS.tick(60)

