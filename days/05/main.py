from dataclasses import dataclass
import sys
from collections import namedtuple
from typing import Any, Dict, List
import math

# Define Point for clarity
Point = namedtuple('Point', 'x y')

@dataclass
class Line:
  p1: Point
  p2: Point

  def __init__(self, p1: Point, p2: Point) -> None:
    self.p1 = p1
    self.p2 = p2


# == Line Utils
def getSlope(line: Line):
  xDiff = line.p2.x - line.p1.x
  if (xDiff == 0):
    return math.nan
  return (line.p2.y - line.p1.y)/xDiff

def isVertical(line: Line):
  return line.p1.x == line.p2.x

def isHorizontal(line: Line):
  return line.p1.y == line.p2.y

def isDiagonal(line: Line) -> bool:
  return not isVertical(line) and not isHorizontal(line)

# Includes last value and guarantees values are sorted
def incAbsRange(v1, v2):
  return range(v2, v1+1) if v2 < v1 else range(v1,v2+1)

def generatePoints(line: Line) -> List[Point]:
  slope = getSlope(line)
  if(math.isnan(slope)):
    return [Point(line.p1.x, y) for y in incAbsRange(line.p1.y, line.p2.y)]
  return [Point(x, slope*(x-line.p1.x)+line.p1.y) for x in incAbsRange(line.p1.x, line.p2.x)]
  


# == File parsing
def parsePoint(text: str) -> Point:
  return Point(*[int(tok) for tok in text.split(',')])

def parseInput(filename) -> List[Line]:
  f = open(filename, "r")
  lines = []
  for line in f:
    text = line.rstrip()
    tokens = text.split()
    point = Line(parsePoint(tokens[0]), parsePoint(tokens[2]))
    lines.append(point)
  return lines

# ==
def sumHazards(map: Dict[Any, int]) -> int:
  hazardPointCount = 0
  for point in map:
    if(map[point] >= 2):
      hazardPointCount += 1
  return hazardPointCount

def findHazards(lines: List[Line]): 
  hazardMap = {}
  for line in lines:
    linePoints = generatePoints(line)
    for point in linePoints:
      if (point not in hazardMap):
        hazardMap[point] = 0
      hazardMap[point] += 1
  return hazardMap

def partOne(data: List[Line]):
  lines = filter(lambda l: not isDiagonal(l), data)
  return sumHazards(findHazards(lines))
  

def partTwo(lines: List[Line]):
  return sumHazards(findHazards(lines))

# Parses input data and and routes to correct solution body
#  May need modified if inputs are read differently between parts
def main(filename: str, part: int):
  data = parseInput(filename)
  answer = (partTwo if part == 2 else partOne)(data)
  print(f"Answer is {answer}.")

# For parsing cli args and starting program
if __name__ == "__main__":
  if(len(sys.argv) < 3):
    print("Exiting, part number and filename must be provided.")
    sys.exit(1)

  partNum = int(sys.argv[1])
  if(partNum != 1 and partNum != 2):
    raise "Part number value must be 1 or 2"

  sys.exit(main(sys.argv[2], partNum))
