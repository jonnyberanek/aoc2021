import sys
from typing import List

NEW_FISH_OFFSET = 2
BIRTH_RATE = 6

class LanternFish():

  daysLeft: int

  def __init__(self) -> None:
    self.daysLeft = BIRTH_RATE + NEW_FISH_OFFSET

  @classmethod
  def fromAbsolute(cls, daysLeft: int):
    fish = LanternFish()
    fish.daysLeft = daysLeft
    return fish
  
  def spawn(self):
    self.daysLeft = BIRTH_RATE
    return LanternFish()

  def spawnReady(self):
    return self.daysLeft < 0
  
  def age(self):
    self.daysLeft -= 1


def parseInput(filename):
  f = open(filename, "r")
  fish = []  
  for text in f.readline().rstrip().split(","):
    daysLeft = int(text)
    fish.append(LanternFish.fromAbsolute(daysLeft))
  return fish


def partOne(fishes: List[LanternFish]):
  for day in range(80):
    print(f"Day {day}")
    for fish in fishes:
      fish.age()
    for fish in fishes:
      if(fish.spawnReady()):
        fishes.append(fish.spawn())
  return len(fishes)

def partTwo(data: List[LanternFish]):
  # Lets keep track of a count per day and continue to add total fish in that bucket
  #  based on when they are birthed
  dayBuckets = [0] * (BIRTH_RATE + 1)
  # Babies (brand new lanternfish) will be put on a rotating queue until 
  # they are mature enough to start spawning; has max size of NEW_FISH_OFFSET
  babies = []
  # Initialize from inputs
  for fish in data:
    dayBuckets[fish.daysLeft] += 1

  for day in range(256):
    # print(f"Day {day} ({(day%7)}), there are {dayBuckets[day%7]} fish that can spawn.")
    babies.append(dayBuckets[day%7])
    if(len(babies) > NEW_FISH_OFFSET):
      dayBuckets[day%7] += babies[0]
      babies = babies[1:]
    # print(dayBuckets, babies)

  # Total all fish together
  total = 0
  for count in dayBuckets:
    total += count
  for count in babies:
    total += count
  return total

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
