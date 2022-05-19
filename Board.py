class Board:
    board=[]
    terminatedPiece = []
    pieces = {'K': 0, 'Q': 1, 'R': 2, 'B': 3, 'N': 4, 'P': 5, 'k': 6, 'q': 7, 'r': 8, 'b': 9, 'n': 10, 'p': 11} #idk you had this number thing in the main file
    boxSize = 90

    # Initializer
    def __init__(self, starting_pos, boxSize):
        self.boxSize = boxSize
        starting_pos = str(starting_pos)
        for i in range(8):
            new_board = []
            for j in range(8):
                new_board.append('-')
            self.board.append(new_board)

        passing = 0

        for i in range(7,-1,-1):
            for j in range(7,-1,-1):
                if passing == 0:
                    char = starting_pos[0]
                    starting_pos = starting_pos[1:]
                    if char == '/':
                        char = starting_pos[0]
                        starting_pos = starting_pos[1:]
                    try:
                        passing = int(char)-1
                    except:
                        self.board[i][j] = char
                else:
                    passing-=1


    def tile_to_number(self,tile):
        letter = tile[0]
        to_num = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
        letter = to_num[letter]
        return letter, int(tile[1])-1

    def get_ded(self):
        ded = self.terminatedPiece
        self.terminatedPiece = []
        return ded

    def get_piece(self,x,y):
        nx = x // self.boxSize
        ny = y // self.boxSize
        return self.board[ny][nx]

    def remove_piece(self,x,y):
        nX = x // self.boxSize
        nY = y // self.boxSize
        self.board[nY][nX] = '-'

    def check_line(self, incX, incY, x, y, legal_moves, color):
        nx = x // self.boxSize
        ny = y // self.boxSize
        nx += incX
        ny += incY
        if color == "black":
            while 0 <= nx <= 7 and 0 <= ny <= 7 and self.board[ny][nx] == '-':
                #print(nx,ny)
                legal_moves.append(str(ny)+str(nx))
                nx += incX
                ny += incY
            return
        elif color == "white":
            while 0 <= nx <= 7 and 0 <= ny <= 7 and self.board[ny][nx] == '-':
                #print(nx,ny)
                legal_moves.append(str(ny)+str(nx))
                nx += incX
                ny += incY
            return

    def check_knight(self, x, y, legal_moves, color):
        nx = x // self.boxSize
        ny = y // self.boxSize
        if 0 <= ny + 1 <= 7 and 0 <= nx + 2 <= 7 and self.color_to_occupy(color, ny + 1, nx + 2):
            legal_moves.append(str(ny+1)+str(nx+2))

        if 0 <= ny - 1 <= 7 and 0 <= nx + 2 <= 7 and self.color_to_occupy(color, ny - 1, nx + 2):
            legal_moves.append(str(ny-1)+str(nx+2))

        if 0 <= ny + 1 <= 7 and 0 <= nx - 2 <= 7 and self.color_to_occupy(color, ny + 1, nx - 2):
            legal_moves.append(str(ny+1)+str(nx-2))

        if 0 <= ny - 1 <= 7 and 0 <= nx - 2 <= 7 and self.color_to_occupy(color, ny - 1, nx - 2):
            legal_moves.append(str(ny-1)+str(nx-2))

        if 0 <= ny + 2 <= 7 and 0 <= nx + 1 <= 7 and self.color_to_occupy(color, ny + 2, nx + 1):
            legal_moves.append(str(ny+2)+str(nx+1))

        if 0 <= ny - 2 <= 7 and 0 <= nx + 1 <= 7 and self.color_to_occupy(color, ny - 2, nx + 1):
            legal_moves.append(str(ny-2)+str(nx+1))

        if 0 <= ny + 2 <= 7 and 0 <= nx - 1 <= 7 and self.color_to_occupy(color, ny + 2, nx - 1):
            legal_moves.append(str(ny+2)+str(nx-1))

        if 0 <= ny - 2 <= 7 and 0 <= nx - 1 <= 7 and self.color_to_occupy(color, ny - 2, nx - 1):
            legal_moves.append(str(ny-2)+str(nx-1))
        #painful

    def check_pawn(self, x, y, legal_moves, first_move, color):
        nx = x // self.boxSize
        ny = y // self.boxSize
        if color == "black":
            if 0 <= ny + 1 <= 7 and self.board[ny + 1][nx].islower() == False:
                legal_moves.append(str(ny + 1) + str(nx))
            if nx <= 1 and self.board[ny + 1][nx - 1].isupper():
                legal_moves.append(str(ny + 1) + str(nx - 1))
            if nx <= 6 and self.board[ny + 1][nx + 1].isupper():
                legal_moves.append(str(ny + 1) + str(nx + 1))
        else:
            if 0 <= ny - 1 <= 7 and self.board[ny - 1][nx].isupper() == False:
                legal_moves.append(str(ny - 1) + str(nx))
            if nx <= 1 and self.board[ny - 1][nx - 1].islower():
                legal_moves.append(str(ny - 1) + str(nx - 1))
            if nx <= 6 and self.board[ny - 1][nx + 1].islower():
                legal_moves.append(str(ny - 1) + str(nx + 1))
        if first_move:
            if color == "black":
                if 0 <= ny + 2 <= 7 and self.board[ny + 2][nx].islower() == False:
                    legal_moves.append(str(ny + 2) + str(nx))
            else:
                if 0 <= ny - 2 <= 7 and self.board[ny - 2][nx].isupper() == False:
                    legal_moves.append(str(ny - 2) + str(nx))

    def check_king(self, x, y, legal_moves, color):
        nx = x // self.boxSize
        ny = y // self.boxSize
        if 0 <= ny + 1 <= 7 and 0 <= nx + 1 <= 7 and self.color_to_occupy(color, ny + 1, nx + 1):
            legal_moves.append(str(ny+1)+str(nx+1))

        if 0 <= ny - 1 <= 7 and 0 <= nx + 1 <= 7 and self.color_to_occupy(color, ny - 1, nx + 1):
            legal_moves.append(str(ny-1)+str(nx+1))

        if 0 <= ny + 1 <= 7 and 0 <= nx - 1 <= 7 and self.color_to_occupy(color, ny + 1, nx - 1):
            legal_moves.append(str(ny+1)+str(nx-1))

        if 0 <= ny - 1 <= 7 and 0 <= nx - 1 <= 7 and self.color_to_occupy(color, ny - 1, nx - 1):
            legal_moves.append(str(ny-1)+str(nx-1))

        if 0 <= ny <= 7 and 0 <= nx - 1 <= 7 and self.color_to_occupy(color, ny, nx - 1):
            legal_moves.append(str(ny)+str(nx-1))

        if 0 <= ny <= 7 and 0 <= nx + 1 <= 7 and self.color_to_occupy(color, ny, nx + 1):
            legal_moves.append(str(ny)+str(nx+1))

        if 0 <= ny + 1 <= 7 and 0 <= nx <= 7 and self.color_to_occupy(color, ny + 1, nx):
            legal_moves.append(str(ny+1)+str(nx))

        if 0 <= ny - 1 <= 7 and 0 <= nx <= 7 and self.color_to_occupy(color, ny - 1, nx):
            legal_moves.append(str(ny-1)+str(nx))

    def color_to_occupy(self, color, y, x):
        if color == "white" and (self.board[y][x].isupper() == False):
            return True
        elif color == "black" and (self.board[y][x].islower() == False):
            return True
        return False

    def set_piece(self,x,y,value):
        nx = x // self.boxSize
        ny = y // self.boxSize
        if self.board[ny][nx] != '-':
            self.terminatedPiece.append(self.pieces[self.board[ny][nx]])
            self.terminatedPiece.append(nx * self.boxSize)
            self.terminatedPiece.append(ny * self.boxSize)
        self.board[ny][nx] = value

    def print_board(self):
        for i in self.board:
            print(i)