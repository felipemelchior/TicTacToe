import sys
import numpy as np

class TicTacToe():
    def __init__(self):
        self.m = 0
        self.n = 0
        self.k = 0
        self.player = 0
        self.gameState = []
        self.getArguments()

    def getArguments(self):
        for i in range(len(sys.argv)):
            if(i == 0):
                pass
            elif(i == 1):
                self.m = int(sys.argv[i])
            elif(i == 2):
                self.n = int(sys.argv[i])
            elif(i == 3):
                self.k = int(sys.argv[i])
            elif(i == 4):
                self.player = int(sys.argv[i])
            else:
                self.gameState.append(int(sys.argv[i]))

        self.gameState = np.reshape(self.gameState, (self.m, self.n))
        
    def printArguments(self):
        print(type(self.m))
        print(self.n)
        print(self.k)

        print()
        for i in self.gameState:
            print(i)
   