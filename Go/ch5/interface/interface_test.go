package interface_test

import (
	"testing"
)

type show interface {
	show() string
}

type Employee struct {
	ID string 
	Name string
	Age int 
}

type Tenant struct {
	ID string
	Name string
}

func (e *Employee) show() string {
	return "fmt.Printf('hello Employee')"
}

func (t *Tenant) show() string {
	return "fmt.Printf('hello Tenant')"
}


func TestObjMethodCall(t *testing.T){
	e1 := new(Employee)
	t.Log(e1.show())
	t1 := new(Tenant)
	t.Log(t1.show())
}

func TestInterface(t *testing.T){
	var p show
	p = new(Employee)
	t.Log(p.show())
	p = new(Tenant)
	t.Log(p.show())
}
