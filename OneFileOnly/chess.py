#!/usr/bin/env python
# coding: utf-8

import sys
import random
import os
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='chess_match.log', encoding='utf-8', level=logging.DEBUG)

#========================UI=======================
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
    print("       _/____\\_   ")
    print("       \\      /   ")
    print("        \\____/    ")
    print("        (____)    ")
    print("         |  |     ")
    print("         |__|     ")
    print("        /    \\    ")
    print("       (______)   ")
    print("      (________)  ")
    print("      //_______\\\\  ")
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
    print("     //__\\    aa    ]8I aa    ]8I")
    print("    ((____)   `\"YbbdP\"\' `\"YbbdP\"\'")



def u_lose():
    print("          ::      ")
    print("        ::::::    ")
    print("          ::      ")
    print("         _()_     ")
    print("       _/____\\_   ")
    print("       \\      /   ")
    print("        \\____/    ")
    print("        (____)    ")
    print("         |  |     ")
    print("         |__|     ")
    print("        /    \\    ")
    print("       (______)   ")
    print("      (________)  ")
    print("      (_________\\\\ ")


def select_color_ui():
    print("          ::      ")
    print("        ::::::    ")
    print("          ::      ")
    print("         _()_     ")
    print("       _/____\\_   ")
    print("       \\      /   ")
    print("        \\____/    ")
    print("        (____)    ")
    print("         |  |     ")
    print("         |__|     ")
    print("        /    \\    ")
    print("       (______)   ")
    print("      (________)  ")
    print("      //_______\\\\ ")
#=================================================

#=====================Board=======================
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
#==================================================


#=====================Pieces=======================
def validate_move(old_piece_position, new_piece_position, board, player_color):
    piece_choosed_dont_even_exit = old_piece_position["row"] < 0 or old_piece_position["row"] > 7 or old_piece_position["column"] < 0 or old_piece_position["column"] > 7
    piece_moved_to_outside_board = new_piece_position["row"] < 0 or new_piece_position["row"] > 7 or new_piece_position["column"] < 0 or new_piece_position["column"] > 7
    
    if piece_moved_to_outside_board or piece_choosed_dont_even_exit:
        return False
    
    piece = board["pieces"][old_piece_position["row"]][old_piece_position["column"] ]
    piece_type = list(piece)[0]
    piece_color = list(piece)[-1]

    piece_moved_is_the_same_color_of_the_player = piece.lower().endswith(player_color[0].lower()) #Is realy your piece?
    if piece_moved_is_the_same_color_of_the_player:
        #old_column = old_position[0]
        #old_row = old_position[1]

        #new_column = new_position[0]
        #new_row = new_position[1]

        column_difference = old_piece_position["column"] - new_piece_position["column"]
        row_difference = old_piece_position["row"] - new_piece_position["row"]
        new_square = board["pieces"][new_piece_position["row"]][new_piece_position["column"]]

        if new_square[-1] == piece[-1]: #Collision: a piece cannot occupy a square already occupied by another piece of the same color.
            return False #Early Break

        column_in_path = old_piece_position["column"]
        row_in_path = old_piece_position["row"]
        free_diagonal_path = True
        free_column_path = True
        free_row_path = True

        while row_in_path != new_piece_position["row"] and column_in_path != new_piece_position["column"]:
            if row_difference != 0:
                row_in_path -= int(row_difference / abs(row_difference))
                piece_row_path = board["pieces"][row_in_path][new_piece_position["column"]]
                if piece_row_path != "*":
                    free_row_path = False
            
            if column_difference != 0:
                column_in_path -= int(column_difference / abs(column_difference))
                piece_column_path = board["pieces"][old_piece_position["row"]][column_in_path]
                if piece_column_path!= "*":
                    free_column_path = False

            if row_difference != 0 and column_difference != 0:
                piece_diagonal_path = board["pieces"][row_in_path][column_in_path]
                if piece_diagonal_path != "*":
                    free_diagonal_path = False
        

        logger.debug('=====Piece Information=====')
        logger.debug(f"Piece: {piece}")
        logger.debug(f"Piece type: {piece_type}")
        logger.debug(f"Corrent Position: {old_piece_position}")
        logger.debug(f"Position to move to: {new_piece_position}")
        logger.debug(f"New Square Piece: {new_square}")
        logger.debug(f"===========================")

        logger.debug(f"=====Position Logs=====")
        logger.debug(f"Column Difference Between Old Position and New Position: {column_difference}")
        logger.debug(f"Row Difference Between Old Position and New Position: {row_difference}")
        logger.debug(f"New Square: {new_square}")
        logger.debug(f"===========================")

        logger.debug(f"=====Path Logs=====")
        logger.debug(f"Pieces in Row Path: {free_row_path}")
        logger.debug(f"Pieces in Column Path: {free_column_path}")
        logger.debug(f"Pieces in Diagonal Path: {free_diagonal_path}")
        logger.debug(f"===========================")

        if (piece_type == 'N'): #Knight
            soma = abs(column_difference) + abs(row_difference)
            if (soma == 3 and column_difference != 0 and row_difference != 0):
                return True
            else:
                return False

        if (piece_type == 'P'): #Pawn
            pawn_capturing = (abs(row_difference) == 1 and abs(column_difference) == 1 and new_square != "*" and new_square[-1] != piece_color)
            pawn_move = (abs(row_difference) == 1 and column_difference == 0 and new_square == "*")
            pawn_first_move = (free_row_path and abs(row_difference) == 2 and column_difference == 0 and new_square == "*" and (old_piece_position["row"] == 1 or old_piece_position["row"]  == 6))
            pawn_only_foward = ((piece == "Pb" and row_difference <= 0) or (piece == "Pw" and row_difference >= 0))
            
            logger.debug(f"======Pawn Information=====")
            logger.debug(f"pawn_capturing: {pawn_capturing}")
            logger.debug(f"pawn_move: {pawn_move}")
            logger.debug(f"pawn_first_move: {pawn_first_move}")
            logger.debug(f"pawn_only_foward: {pawn_only_foward}")
            logger.debug(f"Position Path Row Square: {free_row_path}")
            logger.debug(f"===========================")
            
            if ((pawn_move or pawn_capturing or pawn_first_move) and pawn_only_foward):
                return True
            else:
                return False
            
        if (piece_type == 'B'): #Bishop
            move_in_diagonal = abs(column_difference) == abs(row_difference)
            if move_in_diagonal and free_diagonal_path:
                return True
            else:
                return False
            
        if (piece_type == 'R'): #Rook
            move_in_row_or_column = (abs(column_difference) == 0 != abs(row_difference) == 0)
            if move_in_row_or_column and free_row_path and free_column_path:
                return True
            else:
                return False

def move_a_piece(board, old_position, new_position):

    square_to_move = board["pieces"][new_position["row"]][new_position["column"]]
    if square_to_move == "*":     
        pass
    else:
        board["captured"].append(square_to_move)
    board["pieces"][new_position["row"]][new_position["column"]] = board["pieces"][old_position["row"]][old_position["column"]]
    board["pieces"][old_position["row"]][old_position["column"]] = "*"
    return board

def move_command(command, board, player_color):
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
    for location in locations:
        try:
            #print(location)
            char = list(location)
            positions.append([columns[char[0]], abs(int(char[1])-8)])
        except Exception as e:
            return False
    
    """
    old_column = old_position[0]
    old_row = old_position[1]
    new_column = new_position[0]
    new_row = new_position[1]
    """
    old_piece_position = {
    "column": positions[0][0],
    "row": positions[0][1]
    }
    new_piece_position = {
        "column": positions[1][0],
        "row": positions[1][1]
    }

    if validate_move(old_piece_position, new_piece_position, board, player_color):
        board = move_a_piece(board, old_piece_position, new_piece_position)
        return board
    else:
        return False


def computer_make_a_move(board, dificulty, player_color):
    if dificulty == "super-easy":

        if player_color == "white":
            computer_color = "black"
        else:
            computer_color = "white"

        while True:
            old_piece_position = {
                "column": random.randint(0, 7),
                "row": random.randint(0, 7)
            }
            new_piece_position = {
                "column": random.randint(0, 7),
                "row": random.randint(0, 7)
            }
            if validate_move(old_piece_position=old_piece_position, new_piece_position=new_piece_position, board=board, player_color=computer_color):
                board = move_a_piece(old_position=old_piece_position, new_position=new_piece_position, board=board)
                break
        return board 

#=====================New Game=======================
def new_game(print_format = "ascii", player_color = "white"):
    game = True
    board = create_board()
    coordinates = True
    color_theme = "light"
    invalid = False
    dificulty = "super-easy"
    while game:
        os.system('cls' if os.name == 'nt' else 'clear')
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
                new_board = move_command(command, board, player_color)
                if new_board:
                    board = new_board
                    invalid = False
                else:
                    invalid = True
                    continue
            computer_make_a_move(board, dificulty, player_color)

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

def choose_color_side():
    choice = input("1. White\n2. Black\n3. Random")
    match choice:
        case 1:
            player_color = ("white")
        case 2:
            player_color = ("black")
        case 3:
            player_color = random.choice(["white", "black"])
        case _:
            player_color = ("white")
    return player_color

def options_menu():
    choice = input("1. Dificulty\n2. Sound\n3. Coordinates\n4. Board\n5. Return")
    match choice:
        case 1:
            new_game("ascii", player_color=choose_color_side())
        case 2:
            options_menu()
        case 3:
            sys.exit(0)       

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
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
                player_color = choose_color_side()
                new_game(player_color=player_color)
            case 2:
                options_menu()
            case 3:
                sys.exit(0)
    except KeyboardInterrupt:
            sys.exit(0)

menu()
