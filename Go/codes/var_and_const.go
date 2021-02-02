package codes

import (
	"fmt"
)
const (
	_ = iota
	KB = 1 << (10 * iota)
	MB = 1 << (10 * iota)
	GB = 1 << (10 * iota)
	TB = 1 << (10 * iota)
	PB = 1 << (10 * iota)
)

func Show(){
	fmt.Println(KB,MB,GB,TB,PB)	
}

func Fordemo1(){
	// this is fordemo1 test
	for i := 0; i < 10;i ++ {
		fmt.Println(i)
	}
}
