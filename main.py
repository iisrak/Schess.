from colorama import Fore, Back, Style, init
from game.game import Game
from game.board import Board
from os import system

init()
Board = Board()
Game = Game(Board)

if __name__ == "__main__":
    print("Created by @LaxionDev on replit.com. Still a W.I.P\n\n")
    Board.CreateBoard()

    while True:
        Board.DisplayBoard()
        
        if not Game.Move(input(Style.RESET_ALL + "\n\nMove: ")):
            input("Invalid move. Press 'enter' try again.")

        system("clear")