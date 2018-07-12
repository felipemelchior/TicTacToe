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
        self.gameStates = []
        self.edgeStates = {}
        self.queue = []
        self.maxDepth = 15
        aux = []
        
        #for i in range(self.m):
            #aux.append([])
            #for j in range(self.n):
             #   aux[i].append(self.initialState[(i*self.m) + j])
        
        #self.initialState = aux.copy()

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
    
    def verifyWinRightDiag(self, state, player):
        pass

    def createStates(self, state, player, parent, index1, index2):
        if(state[index1][index2] == 0):
            state[index1][index2] = player
            self.edgeStates[parent].append(len(self.gameStates))
            self.gameStates.append([len(self.gameStates), state.copy()])
            return len(self.gameStates)-1

    def minimax(self, state):
        pass

    def printStates(self):
        for i in self.gameStates:
            print(i)
            print()

    def run(self):
        self.gameStates.append([0, self.initialState])
        self.queue.append(self.gameStates[0][0])
        flag = 1
        flag2 = 1
        depth = 0

        while(self.queue and depth != self.maxDepth):
            auxQueue = self.queue[0]
            self.queue.pop(0)
            currentState = self.gameStates[auxQueue][1]

            self.edgeStates[auxQueue] = []
            zeros = 0
            for i in range(len(currentState)):
                for j in range(len(currentState)):
                    if(currentState[i][j] == 0):
                        zeros += 1

            for z in range(zeros):
                for i in range(len(currentState)):
                    for j in range(len(currentState)):
                        if(currentState[i][j] == 0):
                            if(flag == 1):
                                self.queue.append(self.createStates(currentState, self.player, auxQueue, i, j))
                                flag = 0
                            elif(flag == 0):
                                self.queue.append(self.createStates(currentState, self.opponent, auxQueue, i, j))
                                flag = 1
                            break
                    
            depth += 1

        self.printStates()
