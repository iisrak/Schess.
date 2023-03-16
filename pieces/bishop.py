from game.piece import Piece
from game.helpers import Annotate, UnAnnotate

SpawnLocations = ["02", "05", "72", "75"]

class Bishop(Piece):
    def __init__(self, White: bool, Location: str, Board):
        self.Board = Board
        Piece.__init__(self, White, Location, "b")

    
    def PossibleMoves(self) -> list:
        y = [] 

        #Diagonal (Up+Right)
        z = UnAnnotate(self.Location)
        while True:
            z[0] += 1
            z[1] -= 1
            a = Annotate(z[0],z[1])
            if self.Board.IsPiece(a):
                if self.Board.GetPiece(a).White == self.White:
                    break
            if z[0] <= 7 and z[1] >= 0:
                y.append(a)
            else:
                break         

        #Diagonal (Up+Left)
        z = UnAnnotate(self.Location)
        while True:
            z[0] -= 1
            z[1] -= 1
            a = Annotate(z[0],z[1])
            if self.Board.IsPiece(a):
                if self.Board.GetPiece(a).White == self.White:
                    break
            if z[0] >= 0 and z[1] >= 0:
                y.append(a)
            else:
                break

        #Diagonal (Bottom+Right)
        z = UnAnnotate(self.Location)
        while True:
            z[0] += 1
            z[1] += 1
            a = Annotate(z[0],z[1])
            if self.Board.IsPiece(a):
                if self.Board.GetPiece(a).White == self.White:
                    break
            if z[0] <= 7 and z[1] <= 7:
                y.append(a)
            else:
                break

        #Diagonal (Bottom+Left)
        z = UnAnnotate(self.Location)
        while True:
            z[0] -= 1
            z[1] += 1
            a = Annotate(z[0],z[1])
            if self.Board.IsPiece(a):
                if self.Board.GetPiece(a).White == self.White:
                    break
            if z[0] >= 0 and z[1] <= 7:
                y.append(a)
            else:
                break

        for x in y:
            if x == self.Location:
                y.remove(x)
        
        return y

        