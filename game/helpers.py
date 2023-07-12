from string import ascii_lowercase
from colorama import Fore, Back, Style

_ = True

def UnAnnotate(Annotation: str) -> list:
    "Get coordinates."
    return [ascii_lowercase.index(Annotation[0]), 8-int(Annotation[1])] # Return unannotated (coordinates) version

def Annotate(X: int, Y: int) -> str:
    "Get board annotation."
    return ascii_lowercase[X]+str((8-Y)) # Return annotated version 

def Highlight() -> str:
    "Colouring for the terminal board."
    global _
    _ = not _
    return Style.RESET_ALL + Style.BRIGHT + (Back.BLACK if _ else Back.WHITE) # Black or white color depending on variable