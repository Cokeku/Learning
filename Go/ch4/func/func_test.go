package func_test

import (
	"math/rand"
	"time"
	"testing"
	"fmt"
)



func returnMulitvalues(op int) (res1 int, res2 int){
	return rand.Intn(10),rand.Intn(20)
	
}

func timeSpent(inner func(op int) int)(func (op int) int){
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

func sum(ops ...int) int {
	s := 0
	for _,val := range ops {
		s += val 
	}
	return s 
}

func TestFunc(t *testing.T){
	v1,v2 := returnMulitvalues(2)
	funcSpent:= timeSpent(funcSpent)
	t.Log(funcSpent(10))
	t.Log(v1,v2)
}

func TestVarParma(t *testing.T) {
	t.Log(sum(1,2,3,4))
}

func TestDefer(t *testing.T) {
	// 延迟执行 defer 即使发生panic
	defer func(){
		t.Logf("Clear Resources")
	}()
	t.Logf("Start")
	panic("Eror")
	// 不可达
	t.Logf("End")
}