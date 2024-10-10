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
        border = "\n+---+---+---+---+---+---+---+---+"
        if coordinates:
            coordinates_border = "\n+-a-+-b-+-c-+-d-+-e-+-f-+-g-+-h-+"
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
                        print(abs(8-y), end="")
                    else:
                        print(f"|", end="")
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