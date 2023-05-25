from game.helpers import Annotate, UnAnnotate
from colorama import Fore

Symbols = {
    "r": "♜",
    "n": "♞",
    "b": "♝",
    "q": "♛",
    "k": "♚",
    "p": "♟",
}


class Piece(object):
    def __init__(self, White: bool, Location: str, Initial: str, Board):
        self.Board = Board
        self.Location = Location
        self.Origin = Location
        self.White = White
        self.Initial = Initial
        self.Symbol = (Fore.RED if self.White else Fore.BLUE) + Symbols[Initial]
        self.Pinned = False 


    def Surroundings(self) -> list:
        y = UnAnnotate(self.Location)
        
        x = [
            Annotate(y[0]-1, y[1]-1) if all([not x in self.Location for x in ["a", "8"]]) else None,
            None if "8" in self.Location else Annotate(y[0], y[1]-1),
            Annotate(y[0]+1, y[1]-1) if all([not x in self.Location for x in ["h", "8"]]) else None,
            None if "a" in self.Location else Annotate(y[0]-1, y[1]),
            Annotate(y[0]-1, y[1]+1) if all([not x in self.Location for x in ["a", "1"]]) else None,
            None if "h" in self.Location else Annotate(y[0]+1, y[1]),
            Annotate(y[0]+1, y[1]+1) if all([not x in self.Location for x in ["h", "1"]]) else None,
            None if "1" in self.Location else Annotate(y[0], y[1]+1),
        ]
            
        if not self.White:
            x.reverse()
            
        return x

    
    def HorizontalVertical(self) -> list:
        y = []

        #Up
        z = UnAnnotate(self.Location)
        while True:
            z[1] -= 1
            a = Annotate(z[0],z[1])
            if z[1] >= 0:
                if self.Board.IsPiece(a):
                    y.append(a)
                    break
                y.append(a)
            else:
                break

        #Down
        z = UnAnnotate(self.Location)
        while True:
            z[1] += 1
            a = Annotate(z[0],z[1])
            if z[1] <= 7:
                if self.Board.IsPiece(a):
                    y.append(a)
                    break
                y.append(a)
            else:
                break

       #Left
        z = UnAnnotate(self.Location)
        while True:
            z[0] -= 1
            a = Annotate(z[0],z[1])
            if z[0] >= 0:
                if self.Board.IsPiece(a):
                    y.append(a)
                    break
                y.append(a)
            else:
                break

        #Right
        z = UnAnnotate(self.Location)
        while True:
            z[0] += 1
            a = Annotate(z[0],z[1])
            if z[0] <= 7:
                if self.Board.IsPiece(a):
                    y.append(a)
                    break
                y.append(a)
            else:
                break

        for x in y:
            if x == self.Location:
                y.remove(x)

        return y
    

    def Diagonal(self) -> list:
        y = []

        #Diagonal (Up+Right)
        z = UnAnnotate(self.Location)
        while True:
            z[0] += 1
            z[1] -= 1
            a = Annotate(z[0],z[1])
            if z[0] <= 7 and z[1] >= 0:
                if self.Board.IsPiece(a):
                    y.append(a)
                    break
                y.append(a)
            else:
                break         

        #Diagonal (Up+Left)
        z = UnAnnotate(self.Location)
        while True:
            z[0] -= 1
            z[1] -= 1
            a = Annotate(z[0],z[1])
            if z[0] >= 0 and z[1] >= 0:
                if self.Board.IsPiece(a):
                    y.append(a)
                    break
                y.append(a)
            else:
                break

        #Diagonal (Bottom+Right)
        z = UnAnnotate(self.Location)
        while True:
            z[0] += 1
            z[1] += 1
            a = Annotate(z[0],z[1])
            if z[0] <= 7 and z[1] <= 7:
                if self.Board.IsPiece(a):
                    y.append(a)
                    break
                y.append(a)
            else:
                break

        #Diagonal (Bottom+Left)
        z = UnAnnotate(self.Location)
        while True:
            z[0] -= 1
            z[1] += 1
            a = Annotate(z[0],z[1])
            if z[0] >= 0 and z[1] <= 7:
                if self.Board.IsPiece(a):
                    y.append(a)
                    break
                y.append(a)
            else:
                break

        for x in y:
            if x == self.Location:
                y.remove(x)

        return y 
    

    def __str__(self):
        return self.Symbol
