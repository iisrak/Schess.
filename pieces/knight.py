from game.piece import Piece
from game.helpers import Annotate, UnAnnotate

SpawnLocations = ['01', '06', '71', '76']

class Knight(Piece):
    def __init__(self, White: bool, Location: str, Board):
        Piece.__init__(self, White, Location, 'n', Board)

    
    def PossibleMoves(self) -> list:
        x = UnAnnotate(self.Location)
        y = [(x[0]-2,x[1]-1),
             (x[0]-1,x[1]-2), 
             (x[0]-2,x[1]+1),
             (x[0]-1,x[1]+2), 
             (x[0]+2,x[1]-1), 
             (x[0]+1,x[1]-2),
             (x[0]+2,x[1]+1), 
             (x[0]+1,x[1]+2)]
        
        return [Annotate(z[0],z[1]) for z in y if not any([z[0]<0,z[1]<1,z[0]>7,z[1]>7])]