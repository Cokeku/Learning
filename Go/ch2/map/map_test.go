package map_test

import (
	"testing"
)

func TestInitmap(t *testing.T) {
	// Initmap f1
	m1 := map[int]int{1:1,2:2,3:3}
	t.Log(m1[2])
	t.Logf("m1 len=%d",len(m1))
	// Initmap f2
	m2 := map[int]int{}
	m2[4] = 4
	t.Logf("m2 len=%d",len(m2))
	// Initmap f3
	m3 := make(map[int]int)
	t.Logf("m3 len=%d",len(m3))
}

func TestAcessNotExiting(t *testing.T){
	// map在初始化后会被赋予 0 ；其他编程会被设置为nil
	m1 := map[int]int{}
	m1[1] = 1
	if v,ok := m1[2]; ok {
		t.Logf("key is exiting value's %d",v)
	} else {
		t.Logf("key is not exiting")
	}
}

func TestTravelMap(t *testing.T){
	m1 := map[int]int{1:1,2:2,3:3}
	for k,v := range m1 {
		t.Log(k,v)
	}
}

// Map的Value可以是一个函数来实现工厂模式 
func TestMapwithFunc(t *testing.T){
	m1 := map[int]func(op int)int{}
	m1[1] = func(op int) int {return op}
	m1[2] = func(op int) int {return op*op}
	m1[3] = func(op int) int {return op*op*op}
	t.Log(m1[1](1),m1[2](2),m1[3](3))
}

// 使用Map来实现Set的特性
func TestMapForSet(t *testing.T){
	mySet := map[int]bool{}
	mySet[1] = true
	n := 1
	if mySet[n] {
		t.Logf("%d is exiting",n)
	}else{
		t.Logf("%d is not exiting",n)
	}
	delete(mySet,1)
	n = 1
	if mySet[n] {
		t.Logf("%d is exiting",n)
	}else{
		t.Logf("%d is not exiting",n)
	}
	
}
