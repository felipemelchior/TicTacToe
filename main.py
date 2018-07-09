#!/usr/bin/python3
# -*- coding: utf-8 -*-

###################################################################
#               TRABALHO INTELIGENCIA ARTIFICIAL                  #
#             https://github.com/homdreen/TicTacToe               #
#                                                                 #   
#                                                                 #
#                  FELIPE HOMRICH MELCHIOR                        #
#                        161150758                                #
################################################################### 

from tictactoe import * # Importação do arquivo tictactoe, que possui a classe principal

if __name__ == '__main__': # Funcao que funciona como uma main
    game = TicTacToe() # Instanciação da classe TicTacToe
    #game.printArguments()
    game.verifyWinDiag(2)
    game.printState(game.initialState)
    #game.generateStates()