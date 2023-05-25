from game.piece import Piece
from game.helpers import Annotate, UnAnnotate

SpawnLocations = ["00", "07", "70", "77"] # All the spawning locations for the rook on the board

class Rook(Piece):
    def __init__(self, White: bool, Location: str, Board):
        Piece.__init__(self, White, Location, "r", Board)

    def PossibleMoves(self) -> list:
        "Returns possible moves for rook."
        return self.HorizontalVertical() # Returns all possible horizontal and vertical moves