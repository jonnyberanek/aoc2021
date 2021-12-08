package utils

import (
	"bufio"
	"os"
	"path/filepath"
	"strconv"
)

// Checks for errors and dies
func Check(e error) bool {
	if e != nil {
		panic(e)
	}
	return true
}

// Funs function for each line of a file
func FileForEachLine(filename string, fn func(string)) bool{
	file, err := os.Open(filename)
	Check(err)

	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		fn(scanner.Text())
	}

	return true
}



// Reads CLI args
func ReadCliArgs() (string, int) {
	// Set flags

	args := os.Args[1:]
	if len(args) < 1 {
		panic("Solution part number required.")
	}

	part, err := strconv.ParseInt(args[0], 0, 8)
	Check(err)

	filename := "input.txt"
	if (len(args) > 1) {
		if (args[1] == "test") {
			filename = "test.txt"
		} else {
			filename = args[1]
		}
	} 

	absPath, err := filepath.Abs(filename)
	Check(err)

	return absPath, int(part)
}