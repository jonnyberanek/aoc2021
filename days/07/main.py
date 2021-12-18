import sys
from typing import List

def parseInput(filename):
  f = open(filename, "r")
  crabs = []
  for text in f.readline().rstrip().split(","):
    crabs.append(int(text))
  return crabs

def binary_search(arr, low, high, critFn):
    # Check base case
    if high >= low:
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # Element is not present in the array
        return -1


def partOne(data: List[int]):
  data.sort()
  low = 0
  high = len(arr) - 1
  mid = 0
 
  while low <= high:

      mid = (high + low) // 2

      # If x is greater, ignore left half
      if arr[mid] < x:
          low = mid + 1

      # If x is smaller, ignore right half
      elif arr[mid] > x:
          high = mid - 1

      # means x is present at mid
      else:
          return mid

  # If we reach here, then the element was not present
  return -1

def partTwo(data):
  raise NotImplementedError()

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

