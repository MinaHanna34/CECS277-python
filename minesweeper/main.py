import random
import check_input


def place_mines(board, mines):
  amountOfColumns = len(board)
  amountOfRows = len(board[0])
  count = 0
  while count != mines:
    for i in range(mines):
      randomRow = random.randint(0, amountOfRows - 1)
      randomColumn = random.randint(0, amountOfColumns - 1)

    if board[randomColumn][randomRow] == 0:
      board[randomColumn][randomRow] = 'X'
      count += 1

  return board
""" 
For the funcation place_mines(board, mines). I first used amountofcolums to see how long the board is. I also used amountofrows to count the board and start from 0. I also used count to =0. I used count to see if it's not in the mines. I made a for loop to check index i in the ranges for the mine. I made randomrow generate 0 and the same with randomcolumn. I then used an if statement with board, randomcolumn, and randomrow to see if they have a 0. if they all had a 0 then it would randomly put an X and then count will increase. I then returned board to be able to use it in other functions.



""" 
def count_mines(board):
  amountOfRows = len(board)
  amountOfColumns = len(board[0])

  for i in range(amountOfRows):
    for j in range(amountOfColumns):
      bombsAround = 0
      if board[i][j] != "X":
        row = -1
        while row <= 1:
          col = -1
          while col <= 1:
            try :
              board [i+row][j+col]
              indexrange = True
            except IndexError: 
              indexrange = False
            if indexrange == True:
              if board [i+row][j+col] == "X" and i+row != -1 and j+col != -1:
                bombsAround += 1
            col += 1
          row += 1
        board[i][j] = bombsAround
  return board

""" 
For the funcation count_mines(board). I made amountofrows and amountofcolumns to have the length of the board.I then made a for loop to iterate through the board individually. I made variable bombsaround to keep track of X around the index. I then made an if statement to see if board with index i and was not = x. The nested while was to check the 8 items around the current index and see if they where an x. I also made an expection to counter any IndexErrors. Then I set the board[i][j] = bombsAround and return board.


""" 
def display_board(board):
  for row in board:
    for item in row:
      print(item, end=' ')
    print()
  return
""" 
I used displayboard to be able to display our board using a nested loop. I did for row in board and then for item in row to able to to go through them. Then I printed the items and did return.
""" 
def main():
  print("Minesweeper Maker")
  rows = check_input.get_int_range("Enter number of rows (5-10): ", 5, 10)
  columns = check_input.get_int_range("Enter number of columns (5-10): ",  5, 10)
  mines = check_input.get_int_range("Enter number of mines (5-10): ", 5, 10)

  rowsAndColumns = []

  for i in range(rows):
    rowList = []
    for j in range(columns):
      rowList.append(0)
    rowsAndColumns.append(rowList)
        
  place_mines(rowsAndColumns, mines)
  count_mines(rowsAndColumns)
  display_board(rowsAndColumns)
    

main()
""" 
Our main function was mainly used to print out the user input and the other definitions. I used checkinput to take the user's input and check between 5 and 10. I made an list called rowsandcolumns I used another list called rowlist to insert into rowsandcolumns to create our 2D List. Then I called on all the functions place_mines,count_mines, and display_board.
""" 
