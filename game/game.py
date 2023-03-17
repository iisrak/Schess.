from game.helpers import Annotate, UnAnnotate

class Game:
    def __init__(self, Board):
        self.Board = Board
        self.Turn = True


    def Move(self, Location) -> bool:
        if len(Location) < 2 or len(Location) > 3:
            return False
        elif len(Location) == 2:
            _Location = "p" + Location
        else:
            _Location = Location
            Location = Location[1]+Location[2]
        
        for Piece in (self.Board.White if self.Turn == True else self.Board.Black):
            if not Piece.Initial in _Location: 
                continue 
            else:
                if Location in Piece.PossibleMoves(): 
                    if self.Board.IsPiece(Location):
                        DeadPiece = self.Board.GetPiece(Location)
                        if DeadPiece.White == Piece.White:
                            return False 

                        (self.Board.White if not Piece.White else self.Board.Black).remove(DeadPiece)
                        self.Board.Dead.append(DeadPiece)
                    
                    oldX, oldY = UnAnnotate(Piece.Location)
                    newX, newY = UnAnnotate(Location)
                    
                    self.Board.GameBoard[oldY][oldX] = "."
                    self.Board.GameBoard[newY][newX] = Piece
                    
                    Piece.Location = Location
                    self.Turn = True if self.Turn == False else False
                    return True
        return False

    """def IsKingChecked(self) -> bool:
        for Piece in self.Board.White + self.Board"""