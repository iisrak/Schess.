from game.piece import Piece
from game.helpers import Annotate, UnAnnotate

SpawnLocations = ["03", "73"]

class Queen(Piece):
    def __init__(self, White: bool, Location: str, Board):
        Piece.__init__(self, White, Location, "q", Board)

    
    def PossibleMoves(self) -> list:
        return self.HorizontalVertical() + self.Diagonal()