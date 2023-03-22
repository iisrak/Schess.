from colorama import Fore, Back, Style
from game.game import Game
from game.board import Board
from os import system

Board = Board()
Game = Game(Board)

if __name__ == "__main__":
    print("LaxionDeveloper on github.com and @LaxionDev on repl.it \n\n")
    Board.CreateBoard()

    while True:
        system("clear")
        Board.DisplayBoard()
        
        if not Game.Move(input(Style.RESET_ALL + "\n\nMove: ")):
            input("Invalid move. Press 'enter' try again.")