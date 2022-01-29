"""
Tic Tac Toe Player
"""
from math import inf as infinity
from random import choice
from typing import ByteString
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    count=0
    for i in board:
        for j in i:
            if j !=EMPTY:
                    count+=1
    if count%2 == 0:
        return X
    else:
        return O
    
def actions(board):
    s = set()
    board2 = copy.deepcopy(board)
    for x,y in enumerate(board2):
        for w,z in enumerate(y):
            if z == None:
                s.add((x,w))
    
    return s

def result(board, action):
    if action not in actions(board):
        raise NameError('Action not correct')

    # Make deep copy, chek player and replace action by players
    board2 = copy.deepcopy(board)
    board2[action[0]][action[1]] = player(board)
    return board2


def winner(board):
    if (board[1][1]==board[0][0]) and (board[1][1]==board[2][2]) or (board[1][1]==board[0][2]) and (board[1][1]==board[2][0]) \
    or (board[1][1]==board[1][0]) and (board[1][1]==board[1][2]) or (board[1][1]==board[0][1]) and (board[1][1]==board[2][1]):
        win = board[1][1]
    elif (board[0][1]==board[0][0]) and (board[0][1]==board[0][2]):
        win = board[0][1]
    elif (board[2][1]==board[2][0]) and (board[2][1]==board[2][2]):
        win = board[2][1]
    elif (board[1][0]==board[0][0]) and (board[1][0]==board[2][0]):
        win = board[1][0]
    elif (board[1][2]==board[0][2]) and (board[1][2]==board[2][2]):
        win = board[1][2]
    else:
        win = None
    return win



       

def terminal(board):
    if(winner(board)!=None)or(len(actions(board))==0):
        return True
    else:
        return False

def utility(board):
        if winner(board)==X:
            
            return 1
        elif winner(board)==O:
            
            return -1
        else:
            return 0

def minimax(board):
    if player(board) == X:
        # MAX PLAYER
        opciones = actions(board)
        opcioneslist= []
        valores = []
        for op in opciones:
            valores.append(minValue(result(board,op)))
            opcioneslist.append(op)
        return opcioneslist[valores.index(max(valores))]
             

    elif player(board) == O:
        # MIN PLAYER
        opciones = actions(board)
        valores = []
        opcioneslist = []
        for op in opciones:
            valores.append(maxValue(result(board,op)))
            opcioneslist.append(op)
        return opcioneslist[valores.index(min(valores))]



def minValue(board):
    if terminal(board):
        a = utility(board)
        return a
    else:
        v = infinity
        for action in actions(board):
            v = min(v,maxValue(result(board,action)))
        return  v    


def maxValue(board):
    if terminal(board):
        a = utility(board)
        return a
    else:
        v = -infinity
        for action in actions(board):
            v = max(v,minValue(result(board,action)))
        return  v 