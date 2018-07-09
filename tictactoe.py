import sys
import numpy as np
import copy

class TicTacToe():
    def __init__(self):
        self.m = 0
        self.n = 0
        self.k = 0
        self.player = 0
        self.initialState = []
        self.gamestates = []
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
                self.player = int(sys.argv[i])
            elif(i == 4):
                self.k = int(sys.argv[i])
            else:
                self.initialState.append(int(sys.argv[i]))

        self.initialState = np.reshape(self.initialState, (self.m, self.n))
        
    def printArguments(self):
        print(self.m)
        print(self.n)
        print(self.player)
        print(self.k)
        
        print()
        for i in self.initialState:
            print(i)

    def verifyWinX(self, player):
        sequence = 0
        for i in range(len(self.initialState)):
            for j in range(len(self.initialState)):
                if(self.initialState[i][j] == player):
                    sequence += 1
                else:
                    sequence = 0 
            if(sequence == self.k):
                print(sequence, self.k)
                print(player, "Ganhou!")
                return 1
        return 0

    def verifyWinY(self, player):
        sequence = 0
        for i in range(len(self.initialState)):
            for j in range(len(self.initialState)):
                if(self.initialState[j][i] == player):
                    sequence += 1
                else:
                    sequence = 0  
            if(sequence == self.k):
                print(player, "Ganhou!")
                return 1
            else:
                sequence = 0
        return 0

    def verifyWinDiag(self, player):
        sequence = 0

        for i in range(0, len(self.initialState),1):
            print(self.initialState[i][i])

        return 0

    def getStates(self)

    def printState(self, state):
        print()
        for m in range(len(state)):
            for n in range(len(state)):
                print(state[m][n], " ", end="")
            print()

            
