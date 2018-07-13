import sys # Importação da biblioteca sys, utilizada para o tratamento de argumentos
import copy # Importação da biblioteca copy, utlizada para criar copias de listas

try: # Tratamento de erro da importação da biblioteca Numpy
    import numpy as np # Utilizada para transformar um vetor de entrada, numa matriz mxn
except ImportError: # Se der erro, mostra a mensagem mostrando como instalar o Numpy
    print("ERRO! - Necessário a biblioteca NUMPY\nInstale com - sudo pip3 install numpy")

class TicTacToe(): # Classe principal do programa 
    def __init__(self): # Construtor
        self.m = int(sys.argv[1]) # Quantidade de linhas do tabuleiro
        self.n = int(sys.argv[2]) # Quantidade de colunas do tabuleiro
        self.player = int(sys.argv[3]) # Numero que representa o jogador (1 ou 2)
        self.opponent = 1 if self.player == 2 else 2 # Inverte o numero do jogador, reprensentando o oponente
        self.k = int(sys.argv[4]) # Numero de simbolos em sequencia necessarios para ganhar, condição de vitoria
        self.initialState = [int(i) for i in sys.argv[5:]] # Vetor que representa o estado
        self.play = [] # Jogada que a IA fará
        self.rankMoves = [] # Lista que guarda os movimentos rankeados
        self.initialPoints = 0 # Dicionario que guarda os rankings dos estados
        self.maxDepth = 15 # Altura máxima da arvore

        self.initialState = np.reshape(self.initialState, (self.m, self.n)) # Transforma o vetor em matrix mxn

    def printArguments(self): # Funcao utilizada para o debug inicial
        print(self.m, self.n, self.player, self.opponent, self.k) # Imprime argumentos
        print() # Quebra linha
        for i in self.initialState: # itera sob o estado
            print(i) # imprime o estado

    def verifyWinX(self, state, player): # Funcao que retorna se um dos jogadores ganhou em linhas
        sequence = 0 # Quantidade de simbolos em sequencia
        for i in range(len(state)): # Itera sob o estado recebido
            for j in range(len(state)): # Itera sob o estado recebido
                if(self.initialState[i][j] == player): # Se o simbolo testado for igual ao player recebido
                    sequence += 1 # Aumenta a quantidade de simbolos em sequencia
                else: # Se o simbolo testado for diferente
                    sequence = 0 # Reseta a quantidade de simbolos
                if(sequence == self.k): # Se, em algum momento, a quantidade de simbolos for igual a condição de vitoria
                    return 1 # Retorna 1, que significa que o jogador recebido ganhou
        return 0 # Se alcançar este return, significa que nenhum jogador ganhou

    def verifyWinY(self, state, player):# Funcao que retorna se um dos jogadores ganhou em colunas
        sequence = 0 # Quantidade de simbolos em sequencia
        for i in range(len(state)): # Itera sob o estado recebido
            for j in range(len(state)):  # Itera sob o estado recebido
                if(self.initialState[j][i] == player): # Se o simbolo testado for igual ao player recebido
                    sequence += 1 # Aumenta a quantidade de simbolos em sequencia
                else: # Se o simbolo testado for diferente
                    sequence = 0 # Reseta a quantidade de simbolos
                if(sequence == self.k): # Se, em algum momento, a quantidade de simbolos for igual a condição de vitoria
                    return 1 # Retorna 1, que significa que o jogador recebido ganhou
            sequence = 0 # Quando a coluna muda, ocorre um reset na sequencia de simboloss
        return 0 # Se alcançar este return, significa que nenhum jogador ganhou
    
    def verifyWinRightDiag(self, state, player): # Função que verifica se um dos jogadores ganhou nas diagonais
        sequence = 0 # Quantidade de simbolos em sequencia
        auxRow = 0 # variavel auxiliar para iterar linhas
        auxCol = 0 # variavel auxiliar para iterar colunas

        for i in range(self.m): # itera o estado recebido
            for j in range(self.n): # itera o estado recebido
                auxRow = i # alterado o valor dos auxiliares para o proximo valor inicial a ser testado
                auxCol = j # alterado o valor dos auxiliares para o proximo valor inicial a ser testado
                while((auxRow < self.m and auxCol < self.n)): # Bloco que percorre enquanto as linhas e colunas forem menores que as dimensoes m e n 
                    if(state[auxRow][auxCol] == player): # Se o simbolo testado for igual ao do jogador recebido
                        sequence += 1 # Aumenta a contagem de simbolos
                    else: # Se nao for igual
                        sequence = 0 # Reseta a contagem 
                    if(sequence == self.k): # Se em algum momento a sequencia de simbolos for igual a condição de vitoria
                        return 1 # Retorna 1, que significa vitoria

                    auxRow += 1 # Aumenta a cada iteração do while
                    auxCol += 1 # Aumenta a cada iteração do while
                sequence = 0 # Sempre que sair do while, reseta a contagem de simbolos
        return 0 # Retorna 0, significando que ninguem ganhou

    def verifyWinLeftDiag(self, state, player): # Função que verifica se um dos jogadores ganhou nas diagonais inversas
        sequence = 0 # Quantidade de simbolos em sequencia
        auxRow = 0 # variavel auxiliar para iterar linhas
        auxCol = 0 # variavel auxiliar para iterar colunas

        for i in range(self.m): # itera o estado recebido
            for j in range(self.n-1, -1, -1): # itera o estado recebido, de forma decrescente
                auxRow = i # alterado o valor dos auxiliares para o proximo valor inicial a ser testado
                auxCol = j # alterado o valor dos auxiliares para o proximo valor inicial a ser testado

                while((auxRow < self.m and auxCol >= 0)): # Bloco que percorre enquanto as linhas for menores que a dimensao m e as colunas forem maiores que 0, pois começaram em n-1 
                    if(state[auxRow][auxCol] == player): # Se o simbolo testado for igual ao do jogador recebido
                        sequence += 1 # Aumenta a contagem de simbolos
                    else: # Se nao for igual
                        sequence = 0 # Reseta a contagem 
                    if(sequence == self.k): # Se em algum momento a sequencia de simbolos for igual a condição de vitoria
                        return 1 # Retorna 1, que significa vitoria

                    auxRow += 1 # Aumenta a cada iteração do while
                    auxCol -= 1 # Diminui as colunas a cada iteração do while, pois começaram em n-1 e irao ate 0
                sequence = 0 # Sempre que sair do while, reseta a contagem de simbolos     
        return 0 # Retorna 0, significando que ninguem ganhou

    def verifyWinCondition(self, state): # Função que chama as outras, verificando se alguem ganhou
        if(self.verifyWinX(state, self.player) == 1): # Verifica se o jogador ganhou em linhas
           return 1 # Retorna se ganhou
        if(self.verifyWinY(state, self.player) == 1): # Verifica se o jogador ganhou em colunas
            return 1 # Retorna se ganhou
        if(self.verifyWinRightDiag(state, self.player) == 1): # Verifica se o jogador ganhou em diagonal
            return 1 # Retorna se ganhou
        if(self.verifyWinLeftDiag(state, self.player) == 1):  # Verifica se o jogador ganhou em diagonal inversa
            return 1 # Retorna se ganhou

        if(self.verifyWinX(state, self.opponent) == 1): # Verifica se o oponente ganhou em linhas
            return -1 # Retorna se ganhou
        if(self.verifyWinY(state, self.opponent) == 1): # Verifica se o oponente ganhou em colunas
            return -1 # Retorna se ganhou
        if(self.verifyWinRightDiag(state, self.opponent) == 1): # Verifica se o oponente ganhou em diagonal
            return -1 # Retorna se ganhou
        if(self.verifyWinLeftDiag(state, self.opponent) == 1): # Verifica se o jogador ganhou em diagonal inversa
            return -1 # Retorna se ganhou

        drawCount = 0 # Varivel de contagem de simbolos
        for i in range(self.m): # itera sob o estado recebido
            for j in range(self.n): # itera sob o estado recebido
                if(state[i][j] != 0): # Se o simbolo testado for 1 ou 2
                    drawCount += 1 # Aumenta a contagem de simbolos
        if(drawCount == (self.m * self.n)): # Se a contagem de simbolos for igual a quantidade de simbolos no tabuleiro, significa empate
            return 2 # Retorna empate
 
        return 3 # retorna que o estado ainda esta jogavel

    def getMoves(self, state): # Função que retorna uma lista com os possiveis movimentos
        listMoves = [] # Lista utilizada pela funcao
        for i in range(self.m): # Itera sob o estado recebido
            for j in range(self.n): # itera sob o estado recebido
                if(state[i][j] == 0): # Se a casa testada for 0, significa que nao está sendo utilizada
                    listMoves.append([i,j]) # Adiciona na lista que as coordenadas (i,j) pode ser utilizada para jogar
        return listMoves # retorna a lista

    def sequences(self, state, player): # Função que conta os simbolos que estão em sequencia em todos os modos
        maxCount = 0 # Variavel auxiliar usada para receber qual foi a maior sequencia de simbolos
        count = 0 # Variavel utilizada para contar quantos simbolos existem a cada iteração
        returnValue = 0 # Valor que é incrementada a cada modo
        auxRow = 0 # Utilizada para as diagonais
        auxCol = 0 # Utilizada para as diagonais

        for i in range(len(state)): # Verifica os simbolos em linha
                for j in range(len(state)):
                    if(self.initialState[i][j] == player): # Se a casa testada é igual ao jogador
                       count += 1 # Soma um ao contador
                    else: # Se for diferente
                        maxCount = count # Transfere a maior sequencia para o MaxCount
                        count = 0 # Reseta a contagem
        returnValue += maxCount # Incrementa o valor total com base na maior sequencia de simbolos

        for i in range(len(state)): # Verifica os simbolos em colunas
            for j in range(len(state)):
                if(self.initialState[j][i] == player):
                    count += 1
                else:
                    maxCount = count
                    count = 0
        returnValue += maxCount # Incrementa o valor total com base na maior sequencia de simbolos
        
        for i in range(self.m): # Verifica os simbolos em diagonal
            for j in range(self.n):
                auxRow = i
                auxCol = j
                while((auxRow < self.m and auxCol < self.n)):
                    if(state[auxRow][auxCol] == player):
                        count += 1
                    else:
                        maxCount = count
                        count = 0
                    
                    auxRow += 1
                    auxCol += 1
                count = 0
        returnValue += maxCount # Incrementa o valor total com base na maior sequencia de simbolos

        for i in range(self.m): # Verifica os simbolos em diagonal inversa
            for j in range(self.n-1, -1, -1):
                auxRow = i
                auxCol = j

                while((auxRow < self.m and auxCol >= 0)):
                    if(state[auxRow][auxCol] == player):
                        count += 1
                    else:
                        maxCount = count
                        count = 0
                    
                    auxRow += 1
                    auxCol -= 1
                count = 0
        returnValue += maxCount # Incrementa o valor total com base na maior sequencia de simbolos

        return returnValue # Retorna o valor total

    def heuristic(self, state, depth, player): # Função de heuristica, utilizada para pontuar estados
        if(self.verifyWinCondition(state) == 1): # Se o estado caracteriza vitoria para o jogador
            return self.initialPoints - depth + self.sequences(state, self.player) # Retorna um numero que é a quantidade de movimentos - altura + quantidade de simbolos em sequencia
        elif(self.verifyWinCondition(state) == -1): # Se o estado caracteriza vitoria para o oponente
            return depth - self.initialPoints -1 * (self.sequences(state, self.opponent) * 2) # Retorna altura - quantidade de movimentos - a quantidade de simbolos em sequencia, multiplicado para gerar um numero mais alto
        else: # Se o estado for um empate ou ainda está jogavel
            return self.sequences(state, self.player) - (self.sequences(state, self.opponent)) # retorna uma quantidade de simbolos em sequencia do jogador - a quantidade de simbolos em sequencia do oponente

    def chooseMove(self): # Função que escolhe o movimento com maior pontuação
        maxScore = -1000 # Variavel auxiliar usada para armazenar a maior pontuação
        move = [] # Lista que guarda o movimento com maior pontuação

        for i in self.rankMoves: # Itera na na lista de movimentos rankeados
            if(i[0] > maxScore): # Troca o valor da MaiorPontuação se o movimento a ser testado, tem pontuação maior
                maxScore = i[0]
                move = i[1]

        return move # Retorna o movimento com maior pontuação a ser utilizado

    def maxPlayer(self, state, depth, alpha, beta): # Função MiniMax que maximiza o jogador
        listMoves = self.getMoves(state) # criação da lista de movimentos

        #Se o estado vitoria para alguem, empate ou a altura está no seu numero maximo, a função da heuristica é chamada
        if((self.verifyWinCondition(state) == -1) or (self.verifyWinCondition(state) == 2) or (self.verifyWinCondition(state) == 1) or (depth == self.maxDepth)):
            return self.heuristic(state, depth, self.player) # Chamada da função heuristica

        bestScore = -1000 # Como estamos maximizando o jogador, devemos ter, inicialmente, um numero muito baixo como melhor pontuação
        for move in listMoves: # Itera a cada movimento
            currentState = state.copy() # copia o estado recebido para um novo estado
            currentState[move[0]][move[1]] = self.player # Cria um novo estado com base no movimento testado no momento
            bestScore = max(bestScore, self.minPlayer(currentState, depth+1, alpha, beta)) # Em casos de Max, queremos a maior pontuação, portanto, retornamos o valor maximo para a variavel, entre ela mesmo e a função de minimax que minimiza o oponente.
            alpha = max(alpha, bestScore) # Alpha irá receber a maior pontuação entre o próprio alpha e o melhor resultado retornado pela função anterior
            if(beta <= alpha): # se o alpha for maior que o beta
                break # poda o beta

        return bestScore # Retorna o melhor resultado
 
    def minPlayer(self, state, depth, alpha, beta): # Função MiniMax que minimiza o oponente
        listMoves = self.getMoves(state) # criação da lista de movimentos

        #Se o estado vitoria para alguem, empate ou a altura está no seu numero maximo, a função da heuristica é chamada
        if((self.verifyWinCondition(state) == -1) or (self.verifyWinCondition(state) == 2) or (self.verifyWinCondition(state) == 1) or (depth == self.maxDepth)):
            return self.heuristic(state, depth, self.opponent) # Chamada da função heuristica

        bestScore = 1000 # Como estamos minimizando o oponente, devemos ter, inicialmente, um numero muito alto como melhor pontuação
        for move in listMoves: # Itera a cada movimento
            currentState = state.copy() # copia o estado recebido para um novo estado
            currentState[move[0]][move[1]] = self.opponent # Cria um novo estado com base no movimento testado no momento
            bestScore = min(bestScore, self.maxPlayer(currentState, depth+1, alpha, beta)) # Em casos de Min, queremos a menor pontuação, portanto, retornamos o valor minimo para a variavel, entre ela mesmo e a função de minimax que maximiza o jogador
            beta = min(beta, bestScore) # Beta irá receber o menor valor, entre ele mesmo e o valor retornado da função anterior
            if(beta <= alpha): # Se o alpha for maior que o beta
                break # poda o alpha

        return bestScore # Retona o melhor resultado

    def minimax(self, state, depth, alpha, beta): # Função de minimax que funciona recursivamente alternando entre as funções de minPlayer e maxPlayer 
        listMoves = self.getMoves(state) # criação da lista de movimentos
        
        self.initialPoints = len(listMoves)+1 # Define a quantidade de pontos iniciais
        if len(listMoves) == 1: # Se so existe um movimento possivel
            return [listMoves[0][0], listMoves[0][1]] # Retorna este movimento
        elif len(listMoves) == 0: # Se nao existem movimentos possiveis
            return None # Retorna vazio
        elif len(listMoves) == self.m * self.n: # Se o tabuleiro esta vazio
            return [listMoves[int(len(listMoves)/2)][0], listMoves[int(len(listMoves)/2)][1]] # Para evitar processamento desnecessario, retorna o movimento que esta no centro
        else: # Se existem mais de um movimento, começa o minimax
            bestScore = -1000 # Queremos maximizar o jogador, portanto precisamos de uma pontuação inicial muito baixa.
            for move in listMoves: # Itera na lista de movimentos
                currentState = state.copy() #  copia o estado recebido para um novo estado
                currentState[move[0]][move[1]] = self.player # Cria um novo estado com base no movimento testado no momento
                bestScore = max(bestScore, self.minPlayer(currentState, depth+1, alpha, beta)) # Em casos de Max, queremos a maior pontuação, portanto, retornamos o valor maximo para a variavel, entre ela mesmo e a função de minimax que minimiza o oponente.
                alpha = max(alpha, bestScore) # Alpha receberá o maior valor entre ele mesmo e o melhor resultado retornado da função anterior
                self.rankMoves.append([bestScore, move]) # Adiciona a uma lista, o melhor valor e também o movimento que gerou este valor
                
                self.play = self.chooseMove() # Neste parte, é escolhida, provisoriamente, a jogada que será feita. Conforme a lista acima for aumentando, esta função escolherá o movimento com o maior valor

                if(alpha >= beta): # Se alpha for maior que beta
                    break # poda o beta

        return self.play # Retorna o movimento a ser jogado