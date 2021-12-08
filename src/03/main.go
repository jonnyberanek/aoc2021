package main

import (
	"fmt"
	"utils"
	"03/sol"
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
}
