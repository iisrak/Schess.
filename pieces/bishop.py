from game.piece import Piece
from game.helpers import Annotate, UnAnnotate

SpawnLocations = ["02", "05", "72", "75"] # All the spawning locations for the bishops on the board

class Bishop(Piece):
    def __init__(self, White: bool, Location: str, Board):
        Piece.__init__(self, White, Location, "b", Board)

    def PossibleMoves(self) -> list:
        "Returns possible moves for bishop."
        return self.Diagonal() # Return all possible diagonal moves