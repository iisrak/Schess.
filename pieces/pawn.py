from game.piece import Piece
from game.helpers import Annotate, UnAnnotate

class Pawn(Piece):
    def __init__(self, White: bool, Location: str, Board):
        Piece.__init__(self, White, Location, 'p', Board)

    def PossibleMoves(self) -> list:
        "Returns possible moves for pawn."
        x = [] # Array stores all the possible moves
        y = UnAnnotate(self.Location) # Gets co-ordinates for location
        z = Piece.Surroundings(self) # Array stores all surroundings of the piece (N, NE, E, SE, S, SW, W, NW)
        t = Annotate(y[0], (y[1]+2 if not self.White else y[1]-2)) # Two steps forward, changes depending on color

        if self.Location == self.Origin and not self.Board.IsPiece(t): # Checks if it's in the original position, and if there's not a piece two steps forward
            x.append(t) # Add the two steps to the possible moves if true

        for _ in [z[0], z[2]]: # Loop over NE and NW
            if _ != None and self.Board.IsPiece(_): # Check if there's a piece there
                x.append(_) # Append to possible moves if true

        if z[1] != None and not self.Board.IsPiece(z[1]): # Check if there's not a piece in front of pawn
            x.append(z[1]) # Append to possible moves if true

        return x

    # TO DO: PROMOTION