class Save:
    def __init__(self):
        self.save = []

    def write(self):
        with open("write.txt", "w") as file:
            for i in self.save:
                file.writelines(i+"\n")
        self.save = []

    def read(self):
        self.save = []
        with open("write.txt", "r") as file:
            self.save = file.readlines()
        for i in range(len(self.save)):
            self.save[i] = self.save[i][:-1]


    def add_move(self, oldx, oldy, x, y, piece, boardSize):
        self.save.append(str(oldx//boardSize)+str(oldy//boardSize)+str(piece)+str(x//boardSize)+str(y//boardSize))
        print(self.save)

