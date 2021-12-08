package main

import (
	"fmt"
	"strings"
	"strconv"
	"utils"
)

func part1(filename string) int {
	forward, depth := int(0), int(0)
	
	utils.FileForEachLine(filename, func(text string) {

		splits := strings.Split(text, " ")

		dist, err := strconv.Atoi(splits[1])
		utils.Check(err)

		switch splits[0] {
			case "forward":
				forward += dist
			case "down":
				depth += dist
			case "up":
				depth -= dist
		}
	})
	return forward * depth
}

func part2(filename string) int{
	forward, depth, aim := int(0), int(0), int(0)
	utils.FileForEachLine(filename, func(text string) {

		splits := strings.Split(text, " ")

		value, err := strconv.Atoi(splits[1])
		utils.Check(err)

		switch splits[0] {
			case "forward":
				forward += value
				depth += aim * value
			case "down":
				aim += value
			case "up":
				aim -= value
		}
	})
	return forward * depth
}

func main(){
	filename, _ := utils.ReadCliArgs()

	value := part2(filename)
	fmt.Printf("Value is %d\n", value)
}