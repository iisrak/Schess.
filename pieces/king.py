from game.piece import Piece
from game.helpers import Annotate, UnAnnotate

SpawnLocations = ["04", "74"]

class King(Piece):
    def __init__(self, White: bool, Location: str, Board):
        Piece.__init__(self, White, Location, "k", Board)

        self.Checked = False
        self.MovesMade = []


    def PossibleMoves(self) -> list:
        y = self.Surroundings()
        return y
        """for Piece in (self.Board.White if self.White else self.Board.Black):
            for Location in Piece.PossibleMoves():
                if Location in y:
                    y.remove(Location)

        for z in y:
            if z == None:
                y.remove(z)"""
        


    def LegalMoves(self) -> list:
        y = []        

        #for Piece in (self.Board.White if self.White else self.Board.Black):
            