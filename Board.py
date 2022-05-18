class Board:
    board=[]
    terminated=[]
    pieces = {'K': 0, 'Q': 1, 'R': 2, 'B': 3, 'N': 4, 'P': 5, 'k': 6, 'q': 7, 'r': 8, 'b': 9, 'n': 10, 'p': 11} #idk you had this number thing in the main file
    boxSize = 0
    def __init__(self, starting_pos, boxSize):
        starting_pos = str(starting_pos)
        for i in range(8):
            new_board = []
            for j in range(8):
                new_board.append('-')
            self.board.append(new_board)

        passing = 0
        self.boxSize = boxSize

        for i in range(7,-1, -1):
            for j in range(7,-1, -1):
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

    def get_piece(self,x,y):
        return self.board[y//self.boxSize][x//self.boxSize]

    def remove_piece(self,x,y):
        self.board[y//self.boxSize][x//self.boxSize] = '-'
        print(self.board, x, y)

    def set_piece(self,x,y,value):
        nx = x//self.boxSize
        ny = y//self.boxSize
        if(self.board[ny][nx] != '-'):
            self.terminated.append(self.board[ny][nx])
            self.terminated.append(x)
            self.terminated.append(y)
        self.board[y//self.boxSize][x//self.boxSize] = value

    def get_ded(self):
        ret = self.terminated
        self.terminated = []
        return ret


