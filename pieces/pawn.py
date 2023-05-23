from game.piece import Piece
from game.helpers import Annotate, UnAnnotate

class Pawn(Piece):
    def __init__(self, White: bool, Location: str, Board):
        Piece.__init__(self, White, Location, 'p', Board)

    def PossibleMoves(self) -> list:
        x = UnAnnotate(self.Location)
        y = []
        z = Piece.Surroundings(self)

        if self.Location == self.Origin and not self.Board.IsPiece():
            y = [Annotate(x[0], x[1]+2 if not self.white else x[1]-2)]

        if self.Board.IsPiece(z[0]):
            y.append(z[0])
        if not self.Board.IsPiece(z[1]) and not z[1] in y:
            y.append(z[1])
        if self.Board.IsPiece(z[2]):
            y.append(z[2])
            
        return y

    # TO DO: PROMOTION