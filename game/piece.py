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
    def __init__(self, White: bool, Location: str, Initial: str):
        self.Location = Location
        self.Origin = Location
        self.White = White
        self.Initial = Initial
        self.Symbol = (Fore.RED if self.White == True else Fore.BLUE) + Symbols[Initial]

    
    def Surroundings(self) -> list:
        y = UnAnnotate(self.Location)
        
        tl = Annotate(y[0]-1,y[1]-1) if not "a" in self.Location or "8" in self.Location else None
        tr = Annotate(y[0]+1, y[1]-1) if not "h" in self.Location or "8" in self.Location else None
        bl = Annotate(y[0]-1, y[1]+1) if not "a" in self.Location or "1" in self.Location else None
        br = Annotate(y[0]+1, y[1]+1) if not "1" in self.Location or "h" in self.Location else None
        t = Annotate(y[0], y[1]-1) if not "8" in self.Location else None
        l = Annotate(y[0]-1, y[1]) if not "a" in self.Location else None
        r = Annotate(y[0]+1, y[1]) if not "h" in self.Location else None
        b = Annotate(y[0], y[1]+1) if not "1" in self.Location else None

        x = [tl,t,tr,l,r,bl,b,br]
        
        if not self.White:
            x.reverse()
        return x
    
    
    def __str__(self):
        return self.Initial