from game.piece import Piece
from game.helpers import Annotate, UnAnnotate

SpawnLocations = ["00", "07", "70", "77"]

class Rook(Piece):
    def __init__(self, White: bool, Location: str, Board):
        Piece.__init__(self, White, Location, "r", Board)

    
    def PossibleMoves(self) -> list:
        return self.HorizontalVertical()