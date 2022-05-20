import pygame

class Piece (pygame.sprite.Sprite):
    def __init__(self, newX, newY, ncolor, board, boxSize):
        super().__init__()
        self.x = newX
        self.y = newY
        self.ourX = newX // boxSize
        self.ourY = newY // boxSize
        self.color = ncolor
        self.oldX = newX
        self.oldY = newY
        self.board = board
        self.extended_init()
        self.shouldFollow = False
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.legal_moves = []

    def clear_moves(self):
        self.legal_moves = []

    def extended_init(self):
        pass

    def checkMove(self, boxSize):
        return 1

    def snap(self,boxSize):
        newX = boxSize * (self.x//boxSize)
        newY = boxSize * (self.y//boxSize)
        self.rect.topleft = (newX, newY)
        self.x = newX
        self.y = newY


    def snap_back(self):
        self.rect.topleft = (self.oldX, self.oldY)
        self.x = self.oldX
        self.y = self.oldY

    def setFollow(self,follow):
        self.shouldFollow = follow

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, newX, newY, boxSize):
        if self.shouldFollow:
            self.rect.center = (newX, newY)
            self.x = newX
            self.y = newY

    def move(self, boxSize, peices):
        self.board.board[self.oldY // boxSize][self.oldX // boxSize] = '-'
        for i in peices:
            if i.oldX == self.x and i.oldY == self.y:
                peices.remove(i)
        self.board.board[self.y // boxSize][self.x // boxSize] = self.id

    def checkMove(self, boxSize, pieces, save):
        self.snap(boxSize)
        if str(self.y//boxSize)+str(self.x//boxSize) in self.legal_moves:
            self.move(boxSize, pieces)
            save.add_move(self.oldX, self.oldY, self.x, self.y, self.id, boardSize=boxSize)
            self.oldX = self.x
            self.oldY = self.y
            return True
        return False