#!/usr/bin/python
# import modules used here
from random import randint
import os
import sys

def main():
    print()
    board = []
    board_width = int(input("Choose board width: "))
    board_height = int(input("Choose board height: "))
    number_of_turns = 0
    valid_input = False
    while not valid_input:
      difficulty = input("Choose your difficulty (Easy, Medium, or Hard): ")
      if difficulty == "Easy":
        number_of_turns = int(board_height * board_width - (board_height * board_width / 8))
        valid_input = True
      elif difficulty == "Medium":
        number_of_turns = int(board_height * board_width - (board_height * board_width / 4))
        valid_input = True
      elif difficulty == "Hard":
        number_of_turns = int(board_height * board_width - (board_height * board_width / 2))
        valid_input = True
      else:
        print("Invalid option")
    print()
    print("You have %s turns." % number_of_turns)
    print()
    for x in range(board_height):
        board.append(["O"] * board_width)

    def print_board(board):
        for row in board:
            print(" ".join(row))
        print()
            

    print_board(board)
    print("Turn 1")

    def random_row(board):
        return randint(0, len(board) - 1)

    def random_col(board):
        return randint(0, len(board[0]) - 1)

    ship_row = random_row(board) + 1
    ship_col = random_col(board) + 1
    #print(ship_row)
    #print(ship_col)

    # Everything from here on should go in your for loop!
    # Be sure to indent four spaces!
    for turn in range (number_of_turns):
        guess_col = int(input("Guess Col: "))
        guess_row = int(input("Guess Row: "))
        if guess_row == ship_row and guess_col == ship_col:
            board[guess_row - 1][guess_col -1] = "B"
            print_board(board)
            print("Congratulations! You sunk my battleship!")
            win_ending = input("Press Enter to play again, or any other key to quit: ")
            if win_ending == "":
                os.system('cls' if os.name == 'nt' else 'clear')
                sys.stdout.flush()
                os.execv(sys.executable, ['python'] + [sys.argv[0]])
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                break
        else:
            if (guess_row == 0 or guess_row > board_height) or (guess_col == 0 or guess_col > board_width):
                print("Oops, that's not even in the ocean.")
            elif(board[guess_row - 1][guess_col -1] == "X"):
                print("You guessed that one already.")
            else:
                
    # Print (turn + 1) here!
                print()
                board[guess_row - 1][guess_col - 1] = "X"
                print_board(board)
                print("You missed my battleship!")
                if turn == number_of_turns - 1:
                    print("Game Over")
                    lose_ending = input("Press Enter to retry, or any other key to quit: ")
                    if lose_ending == "":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        sys.stdout.flush()
                        os.execv(sys.executable, ['python'] + [sys.argv[0]])
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                else:
                    print()
                    print("Turn ", turn + 2)
                
if __name__ == '__main__':
  main()


