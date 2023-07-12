from game.helpers import Annotate, UnAnnotate

class Game:
    def __init__(self, Board):
        self.Board = Board # The Board class
        self.Turn = True # Which side turn it is, True = White, False = Black
        self.BKP = '' #Acronym for BlackKingPosition
        self.WKP = '' #Acronym for WhiteKingPosition
        self.MovesMade = [] #For minimax in the future

    def Move(self, Location) -> bool:
        if Location == "undo":
            self.UndoMove()      
            return True

        if len(Location) < 2 or len(Location) > 3:
            return False
        
        Initial = 'p' if len(Location) == 2 else Location[0]
        Location = Location if len(Location) == 2 else Location[1:]

        for Piece in (self.Board.White if self.Turn else self.Board.Black):
            if Piece.Initial != Initial: 
                continue 
            else:
                if Location in Piece.PossibleMoves(): 
                    """if Piece.Pinned:
                        return False"""

                    if self.Board.IsPiece(Location):
                        DeadPiece = self.Board.GetPiece(Location)
                        
                        if DeadPiece.White == Piece.White:
                            return False 

                        (self.Board.White if not Piece.White else self.Board.Black).remove(DeadPiece)
                        self.Board.Dead.append(DeadPiece)
                                      
                    oldX, oldY = UnAnnotate(Piece.Location)
                    newX, newY = UnAnnotate(Location)
                    
                    self.MovesMade.append((Piece.Location, Location))

                    self.Board.GameBoard[oldY][oldX] = '.'
                    self.Board.GameBoard[newY][newX] = Piece
                    
                    Piece.Location = Location
                    self.Turn = not self.Turn                                         
                    
                    return True
        return False
    
   # def KingChecked(self) -> bool:


    def UndoMove(self):
        x = self.MovesMade[-1]
        Piece = self.Board.GetPiece(x[1])

        oldX, oldY = UnAnnotate(x[0]) 
        newX, newY = UnAnnotate(x[1])

        self.Board.GameBoard[oldY][oldX] = Piece
        self.Board.GameBoard[newY][newX] = '.'

        Piece.Location = x[0]

        self.MovesMade.remove(x)
        self.Turn = not self.Turn