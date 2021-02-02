package struct_test

import (
	"unsafe"
	"fmt"
	"testing"
)

// define obj & property
type Employee struct {
	ID string
	Name string
	Age int
}

// define method: arg obj 
func (e Employee) show1() string {
	fmt.Printf("Address is %x", unsafe.Pointer(&e.Name))
	return fmt.Sprintf("hello %s",e.Name)
}

// define method: arg obj pointer
func (e *Employee) show2() string {
	fmt.Printf("Address is %x", unsafe.Pointer(&e.Name))
	return fmt.Sprintf("hello %s",e.Name)
}

func TestCreateEmployeeObj (t *testing.T) {
	// Init
	e1 := Employee{"1","User1",20}
	e2 := Employee{Name:"User2"}
	e2.Age = 18
	e3 := new(Employee)	// get pointer
	e3.Name = "User3"
	t.Log(e1.ID,e2.Name,e2.Age,e3.Name)
	t.Logf("%T %T",e2,e3)
}

func TestStructOperations(t *testing.T){
	// Init 
	e1 := Employee{"1","User10",18}
	fmt.Printf("Address is %x\n", unsafe.Pointer(&e1.Name))
	t.Log(e1.show1())	// arg obj can copy mem
	t.Log(e1.show2())
}