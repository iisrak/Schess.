from game.piece import Piece
from game.helpers import Annotate, UnAnnotate

SpawnLocations = ["02", "05", "72", "75"]

class Bishop(Piece):
    def __init__(self, White: bool, Location: str, Board):
        Piece.__init__(self, White, Location, "b", Board)

    
    def PossibleMoves(self) -> list:
        return self.Diagonal()