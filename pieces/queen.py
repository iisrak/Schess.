from game.piece import Piece
from game.helpers import Annotate, UnAnnotate

SpawnLocations = ["03", "73"] # All the spawning locations for the queens on the board

class Queen(Piece):
    def __init__(self, White: bool, Location: str, Board):
        Piece.__init__(self, White, Location, "q", Board)

    def PossibleMoves(self) -> list:
        "Returns possible moves for queen."
        return self.HorizontalVertical() + self.Diagonal() # Return all possible diagonal moves as well as horizontal and vertical