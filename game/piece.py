from game.helpers import Annotate, UnAnnotate
from colorama import Fore

 # TO DO: DOCUMENT THIS 

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
            Annotate(y[0]-1, y[1]-1) if all([not x in self.Location for x in ("a", "8")]) else None,
            None if "8" in self.Location else Annotate(y[0], y[1]-1),
            Annotate(y[0]+1, y[1]-1) if all([not x in self.Location for x in ("h", "8")]) else None,
            None if "h" in self.Location else Annotate(y[0]+1, y[1]),
            Annotate(y[0]+1, y[1]+1) if all([not x in self.Location for x in ("h", "1")]) else None,           
            None if "1" in self.Location else Annotate(y[0], y[1]+1),
            Annotate(y[0]-1, y[1]+1) if all([not x in self.Location for x in ("a", "1")]) else None,
            None if "a" in self.Location else Annotate(y[0]-1, y[1]),     
        ]
            
        if not self.White:
            x.reverse()
            
        return x

    
    def HorizontalVertical(self) -> list:
        "Return horizontal and vertical moves for pieces such as the queen and rook."        
        y = []
        d = {
            0:(1, -1),
            1:(1, 1), 
            2:(0, -1), 
            3:(0, 1)
        }

        for i in range(4):
            coord = UnAnnotate(self.Location)
            while True:
                coord[d[i][0]] += d[i][1]       
                a = Annotate(coord[0], coord[1])
                if coord[0] >= 0 and coord[0] <= 7 and coord[1] >= 0 and coord[1] <= 7:
                    y.append(a) 
                    if self.Board.IsPiece(a):
                        break
                    continue
                break
                                          
        return [x for x in y if x != self.Location] # Fun fact this function when it was first made was around 70 lines long :), and now it's less than 20

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
