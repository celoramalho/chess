#!/usr/bin/env python
# coding: utf-8

import sys
import random

def print_board(board, format, coordinates, color_theme):#♔♚♕♛♗♝♘♞♙♟♖♜
    pieces = board["pieces"]
    colors = board["colors"]

    if color_theme == "light":
        pieces_ascii = {
            "Pb" : "♟",
            "Rb" : "♜",
            "Nb" : "♞",
            "Bb" : "♝",
            "Qb" : "♛",
            "Kb" : "♚",
            "B" : "|",
            "Pw" : "♙",
            "Rw" : "♖",
            "Nw" : "♘",
            "Bw" : "♗",
            "Qw" : "♕",
            "Kw" : "♔",
            "W" : " ",
            "w": " ",
            "b": "|"       
        }
    if format == "ascii":
        #♔♚♕♛♗♝♘♞♙♟♖♜□■
        border = "+---+---+---+---+---+---+---+---+"
        if coordinates:
            coordinates_border = "+-a-+-b-+-c-+-d-+-e-+-f-+-g-+-h-+"
            print(coordinates_border)
        else:
            coordinates_border = border
            print(border)
        for y, row in enumerate(pieces):
            for x, char in enumerate(row):
                sqr_color = pieces_ascii[(colors[y][x]).lower()]
                if char == "*":
                    print(f"|{sqr_color}{pieces_ascii[colors[y][x]]}{sqr_color}", end="")
                else:
                    print(f"|{sqr_color}{pieces_ascii[char]}{sqr_color}", end="")
                if x == 7:
                    if coordinates:
                        print(abs(8-y), end="\n")
                    else:
                        print(f"|", end="\n")
            if y == 7:
                print(border)
            else:
                print(border)
    elif format == "roots":
        for y, row in enumerate(pieces):
            for x, char in enumerate(row):
                if char == "*":
                    print(f"|{colors[y][x]} |", end="")
                else:
                    print(f"|{char}|", end="")
            print("\n")
#https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode

def u_win():
    print("          ::      ")
    print("        ::::::    ")
    print("          ::      ")
    print("         _()_     ")
    print("       _/____\_   ")
    print("       \      /   ")
    print("        \____/    ")
    print("        (____)    ")
    print("         |  |     ")
    print("         |__|     ")
    print("        /    \    ")
    print("       (______)   ")
    print("      (________)  ")
    print("      //_______\\  ")
    print("       YOU win!  ")

def chess_logo_full():
    print("            88")                                           
    print("            88")                                           
    print("            88")                                        
    print("  ,adPPYba, 88,dPPYba,   ,adPPYba, ,adPPYba, ,adPPYba,") 
    print(" a8\"     \"\" 88P'    \"8a a8P_____88 I8[    \"\" I8[    \"\"")   
    print(" 8b         88       88 8PP\"\"\"\"\"\"\"  `\"Y8ba,   `\"Y8ba,  ")  
    print(" \"8a,   ,aa 88       88 \"8b,   ,aa aa    ]8I aa    ]8I  ") 
    print("  `\"Ybbd8\"' 88       88  `\"Ybbd8\"\' `\"YbbdP\"\' `\"YbbdP\"\'  ")

def chess_logo():
    print("\n            88")                                           
    print("            88")                                           
    print("            88")                                        
    print("  ,adPPYba, 88,dPYba,   ,adPPYba,") 
    print(" a8\"     \"\" 88P'   \"8a a8P_____88")   
    print(" 8b         88      88 8PP\"\"\"\"\"\"\"")  
    print(" \"8a,   ,aa 88      88 \"8b,   ,aa") 
    print("  `\"Ybbd8\"' 88      88  `\"Ybbd8\"\'")
    print("      ___     ,adPPYba, ,adPPYba,")
    print("     ((__)    I8[    \"\" I8[    \"\"")
    print("      |_|     `\"Y8ba,   `\"Y8ba,")
    print("     //__\    aa    ]8I aa    ]8I")
    print("    ((____)   `\"YbbdP\"\' `\"YbbdP\"\'")



def u_lose():
    print("          ::      ")
    print("        ::::::    ")
    print("          ::      ")
    print("         _()_     ")
    print("       _/____\_   ")
    print("       \      /   ")
    print("        \____/    ")
    print("        (____)    ")
    print("         |  |     ")
    print("         |__|     ")
    print("        /    \    ")
    print("       (______)   ")
    print("      (________)  ")
    print("      //_______\\\ ")
    print("       YOU LOSE!  ")

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

    column_difference = old_column - new_column
    row_difference = old_row - new_row

    piece = board["pieces"][old_row][old_column]
    piece_type = list(piece)[0]

    new_square = board["pieces"][new_row][new_column]

    

    

    print(f"Old column: {old_column}\nOld Row: {old_row}\nOld Column type: {type(old_column)}\nRow type: {type(old_row)}\nPiece: {piece}\nRow Difference: {row_difference}\nColumn Difference: {column_difference}\nNew Square: {new_square}")
    print(f"Piece: {piece}\nPiece type: {piece_type}\nNew Square Piece: {new_square}")

    pieces_in_row_path = False
    pieces_in_column_path = False
    path_row_square = old_row
    path_column_square = old_column


    if new_square[-1] == piece[-1]: #Collision: a piece cannot occupy a square already occupied by another piece of the same color.
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
        
        if (abs(column_difference) == 0 and abs(row_difference) != 0 and pieces_in_row_path == False) or (abs(row_difference) == 0 and abs(column_difference) != 0 and pieces_in_column_path == False):
            return True
        else:
            return False

def move_a_piece(board, old_position, new_position):
    old_column = old_position[0]
    old_row = old_position[1]
    new_column = new_position[0]
    new_row = new_position[1]

    square_to_move = board["pieces"][new_row][new_column]
    if square_to_move == "*":     
        pass
    else:
        board["captured"].append(square_to_move)
    board["pieces"][new_row][new_column] = board["pieces"][old_row][old_column]
    board["pieces"][old_row][old_column] = "*"
    return board

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

    if validate_move(old_position, new_position, board):
        board = move_a_piece(board, old_position, new_position)
        return board
    else:
        return False


def computer_make_a_move(board, dificulty):
    if dificulty == "super-easy":
        random_old_position = [random.randint(0, 7) for _ in range(2)]
        random_new_position = [random.randint(0, 7) for _ in range(2)]
        while not validate_move(old_position=random_old_position, new_position=random_new_position, board=board):
            random_old_position = [random.randint(0, 7) for _ in range(2)]
            random_new_position = [random.randint(0, 7) for _ in range(2)]
            board = move_a_piece(old_position=random_old_position, new_position=random_new_position, board=board)
            return board 


def new_game(print_format = "ascii"):
    game = True
    board = create_board()
    coordinates = True
    color_theme = "light"
    invalid = False
    dificulty = "super-easy"
    while game:
        #os.system('cls' if os.name == 'nt' else 'clear')
        try:
            #color_theme = input("What color is your terminal?\n1.Dark\n2.Light")
            print_board(board, print_format, coordinates, color_theme)
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
            computer_make_a_move(board, dificulty)

        except KeyboardInterrupt:
            print("\n      Match aborted")
            sys.exit(0)
    if finished:
        if win:
            u_win()
        else: 
            u_lose()
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
    chess_logo()
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
