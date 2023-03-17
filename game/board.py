from pieces import pawn, knight, queen, bishop, rook, king
from colorama import Fore, Back, Style
from game.helpers import Annotate, UnAnnotate
from string import ascii_lowercase

Color = lambda c: Style.RESET_ALL + Style.BRIGHT + (Back.BLACK if Back.WHITE in c else Back.WHITE)

class Board():
    def __init__(self):
        self.GameBoard = []
        self.White = []
        self.Black = []
        self.Dead = []
        
        for x in range(8):
            self.GameBoard.append(["." for y in range(8)])     

    
    def CreateBoard(self):
        #Add Pawns
        self.GameBoard[1].clear()
        self.GameBoard[6].clear()
        
        for x in range(8):        
            white_Pawn = pawn.Pawn(True, Annotate(len(self.GameBoard[6]), 6), self)
            black_Pawn = pawn.Pawn(False, Annotate(len(self.GameBoard[1]), 1), self)
            
            self.White.append(white_Pawn)
            self.Black.append(black_Pawn)

            self.GameBoard[6].append(white_Pawn)
            self.GameBoard[1].append(black_Pawn)

        #Add Knights
        for Location in knight.SpawnLocations:
            x, y = int(Location[0]), int(Location[1])
            _Knight = knight.Knight(not "0" in Location, Annotate(y, x), self)
            self.GameBoard[x][y] = _Knight
            (self.Black if "0" in Location else self.White).append(_Knight)

        #Add Queen
        for Location in queen.SpawnLocations:
            x, y = int(Location[0]), int(Location[1])
            _Queen = queen.Queen(not "0" in Location, Annotate(y, x), self)
            self.GameBoard[x][y] = _Queen
            (self.Black if "0" in Location else self.White).append(_Queen)

        #Add Bishop
        for Location in bishop.SpawnLocations:
            x, y = int(Location[0]), int(Location[1])
            _Bishop = bishop.Bishop(not "0" in Location, Annotate(y, x), self)
            self.GameBoard[x][y] = _Bishop
            (self.Black if "0" in Location else self.White).append(_Bishop)

        #Add Rook
        for Location in rook.SpawnLocations:
            x, y = int(Location[0]), int(Location[1])
            _Rook = rook.Rook(not ("0" in Location and Location != "70"), Annotate(y, x), self)
            self.GameBoard[x][y] = _Rook
            (self.Black if ("0" in Location and Location != "70") else self.White).append(_Rook)

        #Add King
        for Location in king.SpawnLocations:
            x, y = int(Location[0]), int(Location[1])
            _King = king.King(not "0" in Location, Annotate(y, x), self)
            self.GameBoard[x][y] = _King
            (self.Black if "0" in Location else self.White).append(_King)

    
    def DisplayBoard(self):
        c = Color(Back.WHITE)
        
        for i in range(8):
            print(c+ascii_lowercase[i],end=" ")
        print()
        
        for x in range(8):
            for y in range(8):
                c = Color(c)
                if type(self.GameBoard[x][y]) != str:
                    print(c + self.GameBoard[x][y].Symbol + " ", end="")
                else:
                    print(c + "  ", end="")
                    
            c = Color(c)
            print(str(8 - x))


    def IsPiece(self, Location):
        for Piece in self.White + self.Black:
            if Piece.Location == Location:
                return True
        return False

    
    def GetPiece(self, Location):
        for Piece in self.White + self.Black:
            if Piece.Location == Location:
                return Piece