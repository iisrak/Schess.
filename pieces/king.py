from game.piece import Piece
from game.helpers import Annotate, UnAnnotate

SpawnLocations = ["04", "74"]

HV = {
    0: (1, -1),
    1: (1, 1),
    2: (0, -1),
    3: (0, 1)
} 

D = {
    0:(-1, 1),
    1:(-1, -1), 
    2:(1, 1), 
    3:(1, -1)
}

class King(Piece):
    def __init__(self, White: bool, Location: str, Board):
        Piece.__init__(self, White, Location, "k", Board)

        self.Checked = False
        self.MovesMade = []

    def PossibleMoves(self) -> list:
        y = self.Surroundings()
        return y

    def IsThreatened(self) -> bool:
        for i in range(4):
            coord = UnAnnotate(self.Location)
            while True:
                coord[HV[i][0]] += HV[i][1]       
                a = Annotate(coord[0], coord[1])
                if coord[0] >= 0 and coord[0] <= 7 and coord[1] >= 0 and coord[1] <= 7:
                    if self.Board.IsPiece(a):
                        if self.Board.GetPiece(a).Initial in "qb":
                            return True
                    continue
                break

        for i in range(4):
            coord = UnAnnotate(self.Location)
            while True:
                coord[0] += D[i][0]
                coord[1] += D[i][1]   
                a = Annotate(coord[0], coord[1])
                if coord[0] >= 0 and coord[0] <= 7 and coord[1] >= 0 and coord[1] <= 7:
                    if self.Board.IsPiece(a):
                        if self.Board.GetPiece(a).Initial in "qr":
                            return True
                        break
                    continue
                break
        return False