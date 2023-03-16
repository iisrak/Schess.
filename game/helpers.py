from string import ascii_lowercase

def UnAnnotate(Annotation: str) -> list:
    return [ascii_lowercase.index(Annotation[0]), 8-int(Annotation[1])]

def Annotate(X: int, Y: int) -> str:
    return ascii_lowercase[X]+str((8-Y))