from game.piece import Piece
from game.helpers import Annotate, UnAnnotate

SpawnLocations = ['01', '06', '71', '76'] # All the spawning locations for the knights on the board

class Knight(Piece):
    def __init__(self, White: bool, Location: str, Board):
        Piece.__init__(self, White, Location, 'n', Board)

    def PossibleMoves(self) -> list:
        "Returns possible moves for knight."
        y = UnAnnotate(self.Location) # Gets co-ordinates for location
        x = [
            (y[0]-2,y[1]-1),
            (y[0]-1,y[1]-2), 
            (y[0]-2,y[1]+1),
            (y[0]-1,y[1]+2), 
            (y[0]+2,y[1]-1), 
            (y[0]+1,y[1]-2),
            (y[0]+2,y[1]+1), 
            (y[0]+1,y[1]+2)
            ] # All possible squares that the knight can move to
        
        return [Annotate(z[0],z[1]) for z in x if not any([z[0]<0,z[1]<1,z[0]>7,z[1]>7])] 
        # ^ Returns a new list where it checks boundaries for each of the squares, depending on the validation it'll add them to the list accordingly