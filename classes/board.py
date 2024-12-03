class Board:
    def __init__(self, coordinates = True, format = "ascii"):
        self.board = ["*"*8]*8
        self.coordinates = coordinates
        self.format = format

    def create(self):
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