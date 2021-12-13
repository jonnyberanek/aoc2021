if [ -z "$1" ]
  then
    echo "Day name must be provided."
    exit
fi

cd days

mkdir $1
cd $1

echo 'import sys

def parseInput(filename):
  f = open(filename, "r")
  for rowIdx, line in enumerate(f):
    text = line.rstrip()
    raise NotImplementedError()

def partOne(data):
  raise NotImplementedError()

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
' > main.py

touch input.txt
touch test.txt


