import sys
from dataclasses import dataclass, field
from typing import List
from pprint import pprint

@dataclass
class Tile():
  value: int
  checked: bool

  def __init__(self, value) -> None:
    self.value = value
    self.checked = False

@dataclass
class Board():
  tiles: List[List[Tile]] = field(default_factory=list)

@dataclass
class BingoState():
  picks: List[int] = None
  boards: List[Board] = None

def parseInput(filename) -> BingoState:
  f = open(filename, 'r')
  bingoState = BingoState()
  bingoState.boards = []
  for rowIdx, line in enumerate(f):
    text = line.rstrip()
    if(rowIdx == 0):
      bingoState.picks = [int(value) for value in text.split(',')]
      continue
    if(len(text) == 0):
      bingoState.boards.append(Board())
      continue
    bingoState.boards[-1].tiles.append([Tile(int(value)) for value in text.split()])
  return bingoState
      
def playNumber(boards: List[Board], num: int):
  for board in boards:
    for row in board.tiles:
      for tile in row:
        if(tile.value == num):
          tile.checked = True

def isBoardStateWinning(board: Board) -> bool:
  # Check horizontals
  for row in board.tiles:
    if(all(tile.checked == True for tile in row)):
      return True
  # Check verticals - check i-th item of each row
  for i in range(5):
    column = [tiles[i] for tiles in board.tiles]
    if(all(tile.checked == True for tile in column)):
      return True
  return False

def findFirstWinner(boards: List[Board]) -> Board:
  for board in boards:
    if(isBoardStateWinning(board)):
      return board
  return None

def sumUnchecked(board: Board) -> int:
  sum = 0
  for row in board.tiles:
    for tile in row:
      if(tile.checked == False):
        sum += tile.value
  return sum

def playFirstSquingo(bingoState: BingoState) -> int:
  for pick in bingoState.picks:
    playNumber(bingoState.boards, pick)
    winner = findFirstWinner(bingoState.boards)
    if(winner != None):
      totalUnchecked = sumUnchecked(winner)
      return totalUnchecked * pick
  
def playLastSquingo(bingoState: BingoState) -> int:
  winners: List[Board] = []
  lastPick = None # Track last pick for end calc

  for pick in bingoState.picks:
    playNumber(bingoState.boards, pick)
    lastPick = pick
    for board in bingoState.boards:
      if(isBoardStateWinning(board)):
        winners.append(board)
        bingoState.boards.remove(board)
    # End early if there are no more boards to play
    if(len(bingoState.boards) == 0):
      break
  
  totalUnchecked = sumUnchecked(winners[-1])
  return totalUnchecked * lastPick

def main(filename):
  bingoState = parseInput(filename)
  score = playLastSquingo(bingoState)
  print(f"Winner found! Score is {score}.")

if __name__ == '__main__':
  if(len(sys.argv) < 2):
    print('Exiting, no file given.')
    sys.exit(1)
  sys.exit(main(sys.argv[1]))
