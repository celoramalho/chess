#!/usr/bin/env python
# coding: utf-8

# In[393]:


from board import Board
import string

#https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode


# In[394]:


board = ["*"*8]*8
print(board[1][1])


# In[408]:


def print_board(board, format, color_theme):#♔♚♕♛♗♝♘♞♙♟♖♜
    pieces = board["pieces"]
    colors = board["colors"]
    pieces_ascii = {
        "Pb" : "♟",
        "Rb" : "♜",
        "Nb" : "♞",
        "Bb" : "♝",
        "Qb" : "♛",
        "Kb" : "♚",
        "B" : "■",
        "Pw" : "♙",
        "Rw" : "♖",
        "Nw" : "♘",
        "Bw" : "♗",
        "Qw" : "♕",
        "Kw" : "♔",
        "W" : "□"        
    }
    if format == "ascii":
        #♔♚♕♛♗♝♘♞♙♟♖♜□■
        for y, row in enumerate(pieces):
            for x, char in enumerate(row):
                if char == "*":
                    print(f"|{pieces_ascii[colors[y][x]]}|", end="")
                else:
                    print(f"|{pieces_ascii[char]}|", end="")
            print("\n")
    if format == "roots":
        for y, row in enumerate(pieces):
            for x, char in enumerate(row):
                if char == "*":
                    print(f"|{colors[y][x]} |", end="")
                else:
                    print(f"|{char}|", end="")
            print("\n")

def create_board():
    board_pieces = []
    board_colors = []
    #board = ["*"*8]*8
    #columns = list(string.ascii_lowercase[:8])
    #rows = range(1,8)
    for xindex in range(8):
        line_pieces = []
        line_colors = []
        for yindex in range(8):

            if yindex%2 == xindex%2:
                line_colors.append("W")
            else:
                line_colors.append("B")

            if xindex < 2: #Black
                if xindex == 0:
                    if yindex == 0 or yindex == 7:
                        line_pieces.append("Rb")
                    elif yindex == 1 or yindex == 6:
                        line_pieces.append("Nb")
                    elif yindex == 2 or yindex == 5:
                        line_pieces.append("Bb")
                    elif yindex == 3:
                        line_pieces.append("Qb")
                    elif yindex == 4:
                        line_pieces.append("Kb")

                elif xindex == 1:
                    line_pieces.append("Pb")

            if xindex > 5: #White
                if xindex == 7:
                    if yindex == 0 or yindex == 7:
                        line_pieces.append("Rw")
                    elif yindex == 1 or yindex == 6:
                        line_pieces.append("Nw")
                    elif yindex == 2 or yindex == 5:
                        line_pieces.append("Bw")
                    elif yindex == 3:
                        line_pieces.append("Qw")
                    elif yindex == 4:
                        line_pieces.append("Kw")

                elif xindex == 6:
                    line_pieces.append("Pw")
        
            if xindex > 1 and xindex < 6:
                line_pieces.append("*")
        board_pieces.append(line_pieces)
        board_colors.append(line_colors)
        board = {
            "pieces" : board_pieces,
            "colors" : board_colors
        }
    return board

def new_game(print_format = "ascii"):
    board = create_board()
    #color_theme = input("What color is your terminal?\n1.Dark\n2.Light")
    print_board(board, print_format, color_theme = "Dark")
    


# In[410]:


new_game("ascii")


# In[397]:


def move_a_piece(board, old_loc, new_loc):
    vertical = {
        "a" : 0
        "b" : 1
        "c" : 2
        "d" : 3
        "e" : 4
        "f" : 5
        "g" : 6
        "h" : 7
    }
    horizontal = x - 1

    y = vertical[new_position[0]]
    x = horizontal[new_position[1]]

    new_position = old_position
    old_position = "*"
    return board


# In[33]:


move_a_piece(board, "b2", "b4")


# In[287]:


def cavalo(tab, old_position ,new_position):
    xdiference = new_position[0] - old_position[0]
    ydiference = new_position[1] - old_position[1]
    soma = abs(xdiference) + abs(ydiference)

    if (soma == 3 and xdiference != 0 and ydiference != 0):
        tab[new_position[0]][new_position[1]] = tab[old_position[0]][old_position[1]]
        tab[old_position[0]][old_position[1]] = 0
        print(*tab, sep="\n")
    else:
        print("movimento invalido")


# In[288]:


tab = [[0,0,0,0,0], [0,0,1,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
print(*tab, sep="\n")


# In[290]:


cavalo(tab, [1, 2], [2, 4])


# In[260]:


print(*tab, sep="\n")


# In[ ]:




