from game.piece import Piece
from game.helpers import Annotate, UnAnnotate

class Pawn(Piece):
    def __init__(self, White: bool, Location: str, Board):
        self.Board = Board
        Piece.__init__(self, White, Location, "p")

    def PossibleMoves(self) -> list:
        x = UnAnnotate(self.Location)
        y = []
        if self.Location == self.Origin:
            y = [Annotate(x[0], x[1]+1), Annotate(x[0], x[1]+2)] if not self.White else [Annotate(x[0], x[1]-1), Annotate(x[0], x[1]-2)]

        z = Piece.Surroundings(self)
        if self.Board.IsPiece(z[0]) and self.White != self.Board.GetPiece(z[0]).White:
            y.append(z[0])
        if not self.Board.IsPiece(z[1]) and not z[1] in y:
            y.append(z[1])
        if self.Board.IsPiece(z[2]) and self.White != self.Board.GetPiece(z[2]).White:
            y.append(z[2])
            
        return y

    # TO DO: PROMOTE TO QUEEN