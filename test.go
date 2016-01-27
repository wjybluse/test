package main

import (
	"strconv"
)

func main() {
	var cache = make(map[string]string)
	addChain := make(chan string)
	removeChain := make(chan string)
	for i := 0; i < 100; i++ {
		go func() {
			addChain <- strconv.Itoa(i)
		}()
	}
	for i := 0; i < 100; i++ {
		removeChain <- strconv.Itoa(i)
	}

}
