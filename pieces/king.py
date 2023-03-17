from game.piece import Piece
from game.helpers import Annotate, UnAnnotate

SpawnLocations = ["04", "74"]

class King(Piece):
    def __init__(self, White: bool, Location: str, Board):
        self.Board = Board
        Piece.__init__(self, White, Location, "k")

    def PossibleMoves(self) -> list:
        x = UnAnnotate(self.Location)
        
        return self.Surroundings(self)