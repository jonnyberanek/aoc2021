package main

import (
	"bufio"
	"fmt"
	"math"
	"strconv"

	// "io"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func forEachLine(filename string, fn func(string)){
	file, err := os.Open(filename)
	check(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		fn(scanner.Text())
	}
} 

func part1(filename string) {
	countInc := int(0)
	var lastMeasurement int = math.MaxInt
	forEachLine(filename, func(text string) {
		measurement, err := strconv.Atoi(text)
		check(err)

		if(lastMeasurement < measurement) {
			countInc++
			fmt.Printf("Increase from %d to %d (%d)\n", lastMeasurement, measurement, countInc)
		}
		lastMeasurement = measurement
	})
	fmt.Printf("Depth increased %d times\n", countInc)
}

func sumSubset(arr []int, start int, end int) int{
	sum := int(0)
	for i := start; i < end; i++ {
		sum += arr[i]
	}
	return sum
}

func part2(filename string){
	countInc := int(0)

	queue := make([]int, 0)

	forEachLine(filename, func(text string) {
		measurement, err := strconv.Atoi(text)
		check(err)


		queue = append(queue, measurement)

		fmt.Printf("%v\n", queue)

		if(len(queue) < 4) {
			return
		}

		lastSum := sumSubset(queue, 0,3)
		currentSum := sumSubset(queue, 1,4)

		if(lastSum < currentSum){
			countInc++
			fmt.Printf("Increase from %d to %d (%d)\n", lastSum, currentSum, countInc)
		}

		queue = queue[1:]
		
	})
	fmt.Printf("Depth increased %d times\n", countInc)
}



func main(){
	filename := "test.txt"
	// part1(filename)
	part2(filename)
}