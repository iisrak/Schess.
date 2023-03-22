from game.piece import Piece
from game.helpers import Annotate, UnAnnotate

SpawnLocations = ["04", "74"]

class King(Piece):
    def __init__(self, White: bool, Location: str, Board):
        Piece.__init__(self, White, Location, "k", Board)

    def PossibleMoves(self) -> list:
        #x = UnAnnotate(self.Location)
        
        return self.Surroundings()