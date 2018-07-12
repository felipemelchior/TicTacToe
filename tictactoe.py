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
        self.listMoves = []
        self.gameStates = []
        self.edgeStates = {}
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
    
    def verifyWinRightDiag(self, state, player):
        pass

    def verifyWinLeftDiag(self, state, player):
        pass

    def verifyWinCondition(self, state):
        if(self.verifyWinX(state, self.player) == 1):
            print("Jogador Ganhou")
            return 1
        if(self.verifyWinY(state, self.player) == 1):
            print("Jogador Ganhou")
            return 1
        if(self.verifyWinRightDiag(state, self.player)):
            pass
        if(self.verifyWinLeftDiag(state, self.player)):
            pass

        if(self.verifyWinX(state, self.opponent) == 1):
            print("Oponente Ganhou")
            return -1
        if(self.verifyWinY(state, self.opponent) == 1):
            print("Oponente Ganhou")
            return -1
        if(self.verifyWinRightDiag(state, self.opponent)):
            pass
        if(self.verifyWinLeftDiag(state, self.opponent)):
            pass

        print("Empate")
        return 2

    def getMoves(self, state):
        for i in range(self.m):
            for j in range(self.n):
                if(state[i][j] == 0):
                    self.listMoves.append([i,j])

    def start(self):
        self.getMoves(self.initialState)

        print(self.verifyWinCondition(self.initialState))

        for i in self.listMoves:
            print(i)