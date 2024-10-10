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
        board = {
            "pieces" : board_pieces,
            "colors" : board_colors
        }
    return board

def move_command(command):
    if command:
        try:
            command.split(" ")
            positions = [command[0], command[-1]]
            return positions
        except Exception as e:
            return False
    else:
        return False


def move_piece(locations, board):
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
    positions = []
    for index, location in enumerate(locations):
        char = list(location)
        positions.append([columns[char[0]], abs(int(char[1])-8)])
    print(positions)  


def new_game(print_format = "ascii"):
    game = True
    board = create_board()
    coordinates = True
    color_theme = "light"
    while game:
        #os.system('cls' if os.name == 'nt' else 'clear')
        try:
            #color_theme = input("What color is your terminal?\n1.Dark\n2.Light")
            ui.print_board(board, print_format, coordinates, color_theme)
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
                positions = move_command(command)
                if positions:
                    move_piece(positions, board)
                else:
                    print("Command invalid")
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


tab = [[0,0,0,0,0], [0,0,1,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
print(*tab, sep="\n")


cavalo(tab, [1, 2], [2, 4])

print(*tab, sep="\n")
"""


#Start

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
    os.system('cls' if os.name == 'nt' else 'clear')
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