import sys
import copy

try:
    import numpy as np
except ImportError:
    print("ERRO! - Necessário a biblioteca NUMPY\nInstale com - sudo pip3 install numpy")

class TicTacToe():
    def __init__(self):
        self.m = int(sys.argv[1])
        self.n = int(sys.argv[2])
        self.player = int(sys.argv[3])
        self.opponent = 1 if self.player == 2 else 2
        self.k = int(sys.argv[4])
        self.initialState = [int(i) for i in sys.argv[5:]]
        self.maxDepth = 15
        
        self.initialState = np.reshape(self.initialState, (self.m, self.n))

    def printArguments(self):
        print(self.m, self.n, self.player, self.opponent, self.k) 
        print()
        for i in self.initialState:
            print(i)

    def verifyWinX(self, state, player):
        sequence = 0
        for i in range(len(state)):
            for j in range(len(state)):
                if(self.initialState[i][j] == player):
                    sequence += 1
                else:
                    sequence = 0 
                if(sequence == self.k):
                    print(player, "ganhou")
                    return 1
        return 0

    def verifyWinY(self, state, player):
        sequence = 0
        for i in range(len(state)):
            for j in range(len(state)):
                if(self.initialState[j][i] == player):
                    sequence += 1
                else:
                    sequence = 0  
                if(sequence == self.k):
                    return 1
            else:
                sequence = 0
        return 0
    
    def createStates(self):
        pass

    def verifyWinRightDiag(self, state, player):
        pass

    def minimax(self, state):
        pass
