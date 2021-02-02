package customer_type_test

import (
	"testing"
	"time"
	"fmt"
)
type InitCov func(op int) int

func timeSpent(inner InitCov)(InitCov){
	return func (n int) int {
		now := time.Now()
		ret := inner(n)
		fmt.Println("speet time:",time.Since(now).Seconds())
		return ret
	}
}

func funcSpent(op int) int {
	time.Sleep(time.Second * 1)
	return op
}

func TestFunc(t *testing.T){
	funcSpent:= timeSpent(funcSpent)
	t.Log(funcSpent(10))
}