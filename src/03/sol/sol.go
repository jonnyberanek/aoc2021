package sol

import (
	"fmt"
	"strconv"
	"utils"
)

func Part1(filename string) string {
	counts := make([]int, 0)
	utils.FileForEachLine(filename, func(text string) {
		for pos, char := range text {
			if (len(counts) <= pos) {
				counts = append(counts, 0)
			}
			if (char == '0') {
				counts[pos] -= 1
			}
			if (char == '1') {
				counts[pos] += 1
			}
		}
	})
	gamma := 0
	epsilon := 0
	for pos, count := range counts {
		bitPos := len(counts) - pos - 1
		if (count > 0){
			gamma |= (1 << bitPos)
		} else {
			epsilon  |= (1 << bitPos)
		}
	}
	return fmt.Sprintf("%d", gamma * epsilon)
}

func findByCriteria(candidates []string, criteria func(ones []string, zeroes []string) bool) int64 {
	for pos := 0; pos < len(candidates[0]); pos++ {
		oneBytes := make([]string, 0)
		zeroBytes := make([]string, 0)
		for _, b := range candidates {
			if b[pos] == '1' {
				oneBytes = append(oneBytes, b)
			}
			if b[pos] == '0' {
				zeroBytes = append(zeroBytes, b)
			}
		}
		if (criteria(oneBytes, zeroBytes)){
			candidates = oneBytes
		} else {
			candidates = zeroBytes
		}
		if (len(candidates) == 1) {
			value, err := strconv.ParseInt(candidates[0], 2, 64)
			utils.Check(err)
			return value
		}
	}

	panic("No candidate found")
}

func Part2(filename string) string {
	candidates := make([]string, 0) 
	utils.FileForEachLine(filename, func(text string) {
		candidates = append(candidates, text)
	})
	o2 := findByCriteria(candidates, func(ones, zeroes []string) bool {
		return len(ones) >= len(zeroes)
	})
	co2 := findByCriteria(candidates, func(ones, zeroes []string) bool {
		return len(ones) < len(zeroes)
	})

	return fmt.Sprintf("%d", o2 * co2)
}
