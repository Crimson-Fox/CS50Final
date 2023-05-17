from random import randint
board = []
turn = 0
#builds the grid
for x in range(5):
  board.append(["O"] * 5)

#func to print grid(list of lists)
def print_board(board):
  for row in board:
    print " ".join(row)

#shows board
print_board(board)

#assigns the ship location on any length of grid
def random_row(board):
  return randint(0, len(board) - 1)
def random_col(board):
  return randint(0, len(board[0]) - 1)

#assign vars
ship_row = random_row(board)
ship_col = random_col(board)

#debug print position
print ship_row
print ship_col

#game loop
for turn in range(4):
  print "Turn", turn + 1
  #player input to vars
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  #win checks
  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sunk my battleship!"
    board[guess_row][guess_col] = "#"
    print_board(board)
    break #to pass rest of loop
  else:
    #first checks bounds of guess
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print "Oops, that's not even in the ocean."
    #checks if pre chosen or not
    elif(board[guess_row][guess_col] == "X"):
      print "You guessed that one already."
    #marks guess with X
    else:
      print "You missed my battleship!"
      #assigns the location
      board[guess_row][guess_col] = "X"
    #shows updated grid
    print_board(board)
#Game over check
  if turn == 3:
    print("Game Over")
