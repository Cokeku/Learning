package sync_test

import (
	"sync"
	"testing"
	"fmt"
)

var wg sync.WaitGroup


// func hello(i int) {
// 	defer wg.Done() // goroutine结束就登记-1
// 	fmt.Println("Hello Goroutine!", i)
// }

func TestSync(t *testing.T) {
	for i := 0; i < 10; i++ {
		wg.Add(1) // 启动一个goroutine就登记+1
		go func(i int) {
			defer wg.Done()
			fmt.Println("Hello Goroutine!", i)
		}(i)
	}
	wg.Wait() // 等待所有登记的goroutine都结束
}