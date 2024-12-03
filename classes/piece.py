class Piece:
    def __init__(self, piece_name, position, color) -> None:
        self.piece_name = piece_name
        self.position = position
        self.captured = False
        self.color = color
        self.first_move = True
        self.move_count = 0

    def move_a_piece(self, direction):
    
    def validate_move(self, new_position):
    