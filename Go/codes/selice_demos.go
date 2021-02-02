package codes

import (
	"fmt"
)

func Selice_demo1() {
	fmt.Println("hello world!")
	a := [...]int{1,2,3}
	for ind,val := range a {
		fmt.Println(ind,val)
	}
}
