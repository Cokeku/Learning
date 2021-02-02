package fib_test

import (
	"testing"
)

func TestFib(t *testing.T){
	a := 1
	b := 1
	t.Log(a)
	for i:=0;i < 4;i++{
		t.Log(b)
		a,b=b,a+b
		
	}
}