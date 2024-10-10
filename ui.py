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
            print(border)
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
                print(coordinates_border)
            else:
                print(border)
    if format == "roots":
        for y, row in enumerate(pieces):
            for x, char in enumerate(row):
                if char == "*":
                    print(f"|{colors[y][x]} |", end="")
                else:
                    print(f"|{char}|", end="")
            print("\n")

#https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode