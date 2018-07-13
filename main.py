#!/usr/bin/python3
# -*- coding: utf-8 -*-

###################################################################
#               TRABALHO INTELIGENCIA ARTIFICIAL                  #
#             https://github.com/homdreen/TicTacToe               #
#                                                                 #   
#                                                                 #
#                        REFERÊNCIAS                              #
#                    https://goo.gl/sph4pp                        #
#                    https://goo.gl/rY22sv                        #
#                    https://goo.gl/qVECqR                        #
#                    https://goo.gl/ZPBCQb                        #
#                                                                 #
#                         PARA RODAR                              #
#            $ python3 main.py m n jogador k <estado>             #
#                                                                 #
#                                                                 #
#                                                                 #
#                    FELIPE HOMRICH MELCHIOR                      #
#                          161150758                              #
################################################################### 
# PSEUDOCÓDIGO                                                    #
# function alphabeta(node, depth, α, β, maximizingPlayer) is      #
#     if depth = 0 or node is a terminal node then                #
#         return the heuristic value of node                      #
#     if maximizingPlayer then                                    #
#         v := -∞                                                 #
#         for each child of node do                               #
#             v := max(v, alphabeta(child, depth – 1, α, β,FALSE))#
#             α := max(α, v)                                      #
#             if α ≥ β then                                       #
#                 break (* β cut-off *)                           #
#         return v                                                #
#     else                                                        #
#         v := +∞                                                 #
#         for each child of node do                               #
#             v := min(v, alphabeta(child, depth – 1, α, β, TRUE))#
#             β := min(β, v)                                      #  
#             if α ≥ β then                                       #
#                break (* α cut-off *)                            #
#         return v                                                #
###################################################################

from tictactoe import * # Importação do arquivo tictactoe, que possui a classe principal

if __name__ == '__main__': # Funcao que funciona como uma main
    game = TicTacToe() # Instanciação da classe TicTacToe
    play = game.minimax(game.initialState, -1, -100, 100) # Decisao que a IA fará, um estado inicial e um numero que representa alfa e outro beta, utilizado para a poda
    
    if play: # Se a IA conseguiu calcular uma jogada
        print(play[0], play[1]) # Imprime ela na tela