from pieces import pawn, knight, queen, bishop, rook, king
from game.helpers import Annotate, UnAnnotate, Highlight
from string import ascii_lowercase
from colorama import Style

class Board():
    def __init__(self):
        self.GameBoard = [["." for _ in range(8)] for _ in range(8)] # The gameboard which is a 2D array
        self.White = [] # Array for all white pieces
        self.Black = [] # Array for all black pieces
        self.Dead = []  # Array for any dead pieces
    
    def CreateBoard(self):
        "Creates and initialises the board as well as the pieces."
        #Add Pawns
        self.GameBoard[1].clear() # Clear out row for black pawns
        self.GameBoard[6].clear() # Clear out row for white pawns
        
        for x in range(8):        
            white_Pawn = pawn.Pawn(True, Annotate(len(self.GameBoard[6]), 6), self) # Creates an instance of a white pawn
            black_Pawn = pawn.Pawn(False, Annotate(len(self.GameBoard[1]), 1), self) # Creates an instance of a black pawn
            
            self.White.append(white_Pawn) # Append 'white_pawn' to array for all white pieces
            self.Black.append(black_Pawn) # Append 'black_pawn' to array for all black pieces

            self.GameBoard[6].append(white_Pawn) # Append 'white_pawn' to gameboard array
            self.GameBoard[1].append(black_Pawn) # Append 'black_pawn' to gameboard array

        #Add Knights
        for Location in knight.SpawnLocations: # Loop over all the spawn locations for the knight
            x, y = int(Location[0]), int(Location[1]) # Coordinates for the spawn location
            _Knight = knight.Knight(not "0" in Location, Annotate(y, x), self) # Creates an instance of a knight (the colour of the knight is dependant on the spawn location)
            self.GameBoard[x][y] = _Knight # Replace the placeholder in the gameboard with the knight
            (self.White if _Knight.White else self.Black).append(_Knight) # Append '_Knight' to either 'White' or 'Black' array 

        #Add Queen
        for Location in queen.SpawnLocations: # Loop over all the spawn locations for the queen
            x, y = int(Location[0]), int(Location[1]) # Coordinates for the spawn location
            _Queen = queen.Queen(not "0" in Location, Annotate(y, x), self) # Creates an instance of a queen (the colour of the queen is dependant on the spawn location)
            self.GameBoard[x][y] = _Queen # Replace the placeholder in the gameboard with the queen
            (self.White if _Queen.White else self.Black).append(_Queen) # Append '_Queen' to either 'White' or 'Black' array 

        #Add Bishop
        for Location in bishop.SpawnLocations: # Loop over all the spawn locations for the bishop
            x, y = int(Location[0]), int(Location[1]) # Coordinates for the spawn location
            _Bishop = bishop.Bishop(not "0" in Location, Annotate(y, x), self) # Creates an instance of a bishop (the colour of the bishop is dependant on the spawn location)
            self.GameBoard[x][y] = _Bishop # Replace the placeholder in the gameboard with the bishop
            (self.White if _Bishop.White else self.Black).append(_Bishop) # Append '_Bishop' to either 'White' or 'Black' array 

        #Add Rook
        for Location in rook.SpawnLocations: # Loop over all the spawn locations for the rook
            x, y = int(Location[0]), int(Location[1]) # Coordinates for the spawn location
            _Rook = rook.Rook(not ("0" in Location and Location != "70"), Annotate(y, x), self) # Creates an instance of a rook (the colour of the rook is dependant on the spawn location)
            self.GameBoard[x][y] = _Rook # Replace the placeholder in the gameboard with the rook
            (self.White if _Rook.White else self.Black).append(_Rook) # Append '_Rook' to either 'White' or 'Black' array 

        #Add King
        for Location in king.SpawnLocations: # Loop over all the spawn locations for the king
            x, y = int(Location[0]), int(Location[1]) # Coordinates for the spawn location
            _King = king.King(not "0" in Location, Annotate(y, x), self) # Creates an instance of a king (the colour of the king is dependant on the spawn location)
            self.GameBoard[x][y] = _King # Replace the placeholder in the gameboard with the king
            (self.White if _King.White else self.Black).append(_King) # Append '_King' to either 'White' or 'Black' array 
            
            if _King.White: # Checks if white king
                self.WhiteKing = _King # Set variable accordingly
            else: 
                self.BlackKing = _King # Set variable accordingly
  
    def DisplayBoard(self):
        "Display the game board in the terminal."
        for i in range(8):
            print(ascii_lowercase[i], end=" ") # Output the letters
        print() # Create a new line
        for i in range(8):
            for Item in self.GameBoard[i]: # Loops over all the items in the board
                print(Highlight() + str(Item), end=" ") # Output the items
            print(Highlight() + Style.RESET_ALL + f" {str(8-i)}") # Output the numbers

    def IsPiece(self, Location) -> bool:
        "Returns boolean on whether a piece exists in a specific location."
        try:
            x = UnAnnotate(Location) # Get coordinates 
            return type(self.GameBoard[x[1]][x[0]]) != str # Return whether the value is a string or not, that way we're able to identify if it's a piece or not
        except IndexError:
            return False
    
    def GetPiece(self, Location):
        "Returns piece in specific location."
        try:
            x = UnAnnotate(Location) # Get coordinates of piece
            return self.GameBoard[x[1]][x[0]] # Return piece 
        except TypeError:
            return False 