base_pkg=aoc2021

if [ -z "$1" ]
  then
    echo "Day name must be provided."
    exit
fi

cd src

mkdir $1
cd $1

echo 'package main

import (
	"fmt"
	"utils"
	"'$1'/sol"
)

func pickPart(part int) func(string) string {
	if (part == 1){
		return sol.Part1
	} else if (part == 2) {
		return sol.Part2
	}
	panic(fmt.Sprintf("Part %d does not exist", part))
}

func main(){
	filename, part := utils.ReadCliArgs()

	value :=  pickPart(part)(filename)
	fmt.Printf("Answer is %s\n", value)
}' > main.go

mkdir sol
echo 'package sol

func Part1(filename string) string {
	return filename
}

func Part2(filename string) string {
	return filename
}' > sol/sol.go

touch input.txt
touch test.txt


