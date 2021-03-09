import ast 
from collections import deque
import numpy as np 


visited_tiles = []

#allowed moves as per problem.Only up, down right, left. No diagonals
moves = [(1,0),(0,1),(-1,0),(0,-1)]


def printBoard(board):
  for row in board:
    for i in row:
      print('{:^5}'.format(i), end='')
    print()

def getMatrix(nRows, nCols, vals):
  assert nRows*nCols == len(vals), "value count is not matching matrix size"
  board = np.array(vals)
  board = board.reshape(nRows, nCols)
  return board

def availableTiles(pos, nRows, nCols):
  at = []
  for move in moves:
    x = move[0] + pos[0]
    y = move[1] + pos[1]
    if 0 <= x < nRows:
      if 0 <= y < nCols:
        if (x,y) not in visited_tiles:
          at.append((x, y))
  return at


def game(data):
  nRows = data[0]
  nCols = data[1]
  vals = data[2]

  #Convert in value in matrix to represent the board
  print("------ Given Board ------")
  board = getMatrix(nRows, nCols, vals)
  printBoard(board)
  is_possible = False

  #Get start pos and end pos
  try:
    start_idx = vals.index(1)
    vals.index(2)
  except ValueError:
    print('Start and End Positions are required')
    return

  start_pos = ( start_idx//nCols, start_idx % nCols )
  visited_tiles.append(start_pos)
  
  #run on the board from start pos to all possible tiles till end pos
  avail_tiles = deque() 
  avail_tiles.extend(availableTiles(start_pos, nRows, nCols))

  while len(avail_tiles) > 0:
    tile = avail_tiles.pop()
    if board[tile] != -1:
      visited_tiles.append(tile)
    if board[tile] == 2:
      is_possible = True
      break
    elif board[tile] == 0:
      avail_tiles.extend(availableTiles(tile, nRows,nCols))
    
    
  return is_possible 



# ----- Main Function Starts here ------

# input_str = "[nRows,nCols,[val for each cell]]"

#Sample input str for success
input_str = "[4,5,[0,0,0,0,0,1,0,-1,0,-1,0,0,-1,-1,-1,0,0,2,0,0]]"

#Sample input str for failue 
# input_str = "[4,5,[0,0,0,-1,0,1,0,-1,2,-1,0,0,-1,-1,-1,0,0,0,0,0]]"

data= ast.literal_eval(input_str)

sol = game(data)
if sol:
  print('Success')
else:
  print('Failure')
