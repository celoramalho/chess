#!/usr/bin/env python
# coding: utf-8

from board import Board
import string
import ui
import os
import sys

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
        captured = []
        board = {
            "pieces" : board_pieces,
            "colors" : board_colors,
            "captured": captured
        }
    return board

def validate_move(old_position, new_position, board):
    
    old_column = old_position[0]
    old_row = old_position[1]
    new_column = new_position[0]
    new_row = new_position[1]
    piece = board["pieces"][old_row][old_column]
    piece_type = list(piece)[0]
    print(f"Piece: {piece}\nPiece type: {piece_type}")
    new_square = board["pieces"][new_row][new_column]
    column_difference = old_column - new_column
    row_difference = old_row - new_row

    

    print(f"Old column: {old_column}\nOld Row: {old_row}\nOld Column type: {type(old_column)}\nRow type: {type(old_row)}\nPiece: {piece}\nRow Difference: {row_difference}\nColumn Difference: {column_difference}\nNew Square: {new_square}")
    print(new_square)


    pieces_in_row_path = False
    path_row_square = old_row
    path_column_square = old_column


    if new_square[-1] == piece[-1]: #Collision, cant go to a oc
        return False

    while path_row_square != new_row:
        path_row_square -= int(row_difference / abs(row_difference))
        print(f"Path row square: {path_row_square}")
        position_path_row_square = board["pieces"][path_row_square][new_column]
        print(position_path_row_square)
        if position_path_row_square != "*":
           pieces_in_row_path = True
 
    while path_column_square != new_column:
        path_column_square -= int(column_difference / abs(column_difference))
        position_path_column_square = board["pieces"][new_row][path_column_square]
        if position_path_column_square != "*":
            pieces_in_column_path = True
    
    if (piece_type == 'N'):
        soma = abs(column_difference) + abs(row_difference)
        if (soma == 3 and column_difference != 0 and row_difference != 0):
            return True
        else:
            return False

    if (piece_type == 'P'):
        print("Peão")
        print(abs(column_difference))
        pawn_capturing = (abs(row_difference) == 1 and abs(column_difference) == 1 and new_square != "*")
        pawn_move = (abs(row_difference) == 1 and column_difference == 0 and new_square == "*")
        pawn_first_move = ( not pieces_in_row_path and abs(row_difference) == 2 and column_difference == 0 and new_square == "*" and (old_row == 1 or old_row == 6))
        pawn_only_foward = ((piece == "Pb" and row_difference <= 0) or (piece == "Pw" and row_difference >= 0))
        print(f"Pawn capturing: {pawn_capturing}\nPawn Move: {pawn_move}\nPawn First move: {pawn_first_move}\nPawn Only Foward: {pawn_only_foward}\nPosition Path Row Square: {pieces_in_row_path }")
        if ((pawn_move or pawn_capturing or pawn_first_move) and pawn_only_foward):
            return True
        else:
            return False
    if (piece_type == 'B'):
        if (abs(column_difference) == abs(row_difference)):
            return True
        else:
            return False
        
    if (piece_type == 'R'):
        
        if (abs(column_difference) == 0 and abs(row_difference) != 0) or (abs(row_difference) == 0 and abs(column_difference) != 0):
            return True
        else:
            return False



def move_command(command, board):
    columns = {
        "a" : 0,
        "b" : 1,
        "c" : 2,
        "d" : 3,
        "e" : 4,
        "f" : 5,
        "g" : 6,
        "h" : 7
    }
    if command:
        try:
            command = command.split(" ") #print(f"Commands: {command}")
            locations = [command[0], command[-1]]
        except Exception as e:
            return False
    else:
        return False
    positions = []
    #print(f"Locations: {locations}")
    for index, location in enumerate(locations):
        try:
            #print(location)
            char = list(location)
            positions.append([columns[char[0]], abs(int(char[1])-8)])
        except Exception as e:
            return False
    

    old_position = positions[0]
    new_position = positions[1]
    old_column = old_position[0]
    old_row = old_position[1]
    new_column = new_position[0]
    new_row = new_position[1]

    if validate_move(old_position, new_position, board):
        square_to_move = board["pieces"][new_row][new_column]
        if square_to_move == "*":     
            pass
        else:
            board["captured"].append(square_to_move)
        board["pieces"][new_row][new_column] = board["pieces"][old_row][old_column]
        board["pieces"][old_row][old_column] = "*"
        return board
    else:
        return False

def new_game(print_format = "ascii"):
    game = True
    board = create_board()
    coordinates = True
    color_theme = "light"
    invalid = False
    while game:
        #os.system('cls' if os.name == 'nt' else 'clear')
        try:
            #color_theme = input("What color is your terminal?\n1.Dark\n2.Light")
            ui.print_board(board, print_format, coordinates, color_theme)
            if invalid:
                print("*Invalid input*")
            else:
                print("")
            command = input("Command: ").lower()
            finished = True

            if command == "exit" or command == "end":
                finished = False
                game = False
            elif not coordinates and command.split(" ")[0] == "coordinates" or command == 'coordinates on':
                coordinates = True
            elif coordinates and command.split(" ")[0] == "coordinates" or command == 'coordinates off':
                coordinates = False
            elif command == "surrender" or command == "/f":
                win = False
                game = False
            else:
                new_board = move_command(command, board)
                if new_board:
                    board = new_board
                    invalid = False
                else:
                    invalid = True
                    continue

        except KeyboardInterrupt:
            print("\n      Match aborted")
            sys.exit(0)
    if finished:
        if win:
            ui.u_win()
        else: 
            ui.u_lose()
    else:
        print("Match aborted")
"""
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

move_a_piece(board, "b2", "b4")

"""



#tab = [[0,0,0,0,0], [0,0,1,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
#print(*tab, sep="\n")


#cavalo(tab, [1, 2], [2, 4])

#print(*tab, sep="\n")
"""


#Start
"""
def options_menu():
    choice = input("1. Dificulty\n2. Sound\n3. Coordinates\n4. Board\n5. Return")
    match choice:
        case 1:
            new_game("ascii")
        case 2:
            options_menu()
        case 3:
            sys.exit(0)

def menu():
    #os.system('cls' if os.name == 'nt' else 'clear')
    ui.chess_logo()
    try: 
        choice = input("\n\n            1. New Game\n            2. Options\n            3. Exit\n").strip()
        print(f"a{choice}a")
        try:
           choice = int(choice)
        except Exception as e:
            raise RuntimeError("Não foi possivél converter pra número")
        match choice:
            case 1:
                new_game()
            case 2:
                options_menu()
            case 3:
                sys.exit(0)
    except KeyboardInterrupt:
            sys.exit(0)


menu()
