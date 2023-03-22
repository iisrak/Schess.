from game.helpers import Annotate, UnAnnotate

class Game:
    def __init__(self, Board):
        self.Board = Board
        self.Turn = True
        self.BKP = "" #Acronym for BlackKingPosition
        self.WKP = "" #Acronym for WhiteKingPosition


    def Move(self, Location) -> bool:
        if len(Location) < 2 or len(Location) > 3:
            return False
        
        Initial = "p" if len(Location) == 2 else Location[0]
        Location = Location if len(Location) == 2 else Location[1:]
        
        for Piece in (self.Board.White if self.Turn == True else self.Board.Black):
            if Piece.Initial != Initial: 
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
                    self.Turn = not self.Turn                 

                    

                    return True
        return False


    def IsKingChecked(self) -> bool:
        for Piece in (self.Board.White if self.Turn else self.Board.Black):
            if Piece.Location == (self.WKP if self.Turn else self.BKP):
                pass