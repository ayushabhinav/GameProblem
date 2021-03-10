import numpy as np

class Game(object):

  __target_val = 2
  __start_val  =  1
  __danger_val = -1
  __allow_val  = 0

  __moves = {
            'left' : (0, -1),
            'right': (0, 1),
            'up' : (1, 0),
            'down' : (-1, 0)
          }

  def __init__(self, nRows, nCols, val_list):
    self.nRows = nRows
    self.nCols = nCols
    self.vals = val_list
    assert self.nRows * self.nCols == len(self.vals), 'Please provide values for all cells'
    self.board = self._getMatrix(self.nRows, self.nCols, self.vals)
    self.visited_tiles = set()
    self.path = []


  def _getMatrix(self, nRows, nCols, vals):
    return np.array(vals, dtype='int').reshape([nRows, nCols])


  def _solved(self, pos):
    for val in self.__moves.values():
      new_pos = (pos[0] + val[0], pos[1] + val[1])
      if 0 <= new_pos[0] < self.nRows:
        if 0 <= new_pos[1] < self.nCols:
          if self.board[new_pos] == self.__target_val:
            return True
    return False



  def _availableTiles(self, pos):
    at = []
    for move in self.__moves.values():
      x = move[0] + pos[0]
      y = move[1] + pos[1]
      if 0 <= x < self.nRows:
        if 0 <= y < self.nCols:
          # print(x,y)
          if self.board[(x,y)] != self.__danger_val and (x,y) not in self.visited_tiles:
            at.append((x, y))
    # print(f'Available Path -> {at}')
    return at


  def __solve(self, pos):

    self.path.append(pos)
    self.visited_tiles.add(pos)
    if self._solved(pos):
      return True

    # print(f'Path ------------------------> {self.path}')
    # print(f'Visited ->{self.visited_tiles}')

    for tile in self._availableTiles(pos):
      # print(f'Current Pos -> {tile}')
      if self.__solve(tile):
        return True

      self.path.pop()
    return False




  def solve(self):
    start_idx = self.vals.index(self.__start_val)
    start_pos = (start_idx//self.nCols, start_idx % self.nCols)

    end_idx = self.vals.index(self.__target_val)
    end_pos = (end_idx//self.nCols, end_idx % self.nCols)

    # self.visited_tiles.add(start_pos)
    # self.path.append(start_pos)

    if self.__solve(start_pos):
      self.path.append(end_pos)
      return (True, self.path)
  
    return (False, [])


  def show_board(self):
    for row in self.board:
      for cell in row:
        print('{:^5}'.format(cell), end=' ')
      print()




# --------- Main fuction starts here --------- 
nRows = 4
nCols = 5

#Sample val where solution exist
vals = [0,0,0,0,0,1,0,-1,0,-1,0,0,-1,-1,-1,0,0,2,0,0]

#Sample val where solution doesnot exist
# vals = [0,0,0,-1,0,1,0,-1,2,-1,0,0,-1,-1,-1,0,0,0,0,0]

g = Game(nRows, nCols, vals)
print('-' * 20 )
g.show_board()
print('-' * 20 )
is_success, path = g.solve()
if is_success:
  print('Solution Exist? Yes')
  print(f'Path :{path}')
else:
  print('Solution Exist? No')
