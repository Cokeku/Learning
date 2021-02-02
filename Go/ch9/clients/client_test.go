package clients_test

import (
	"github.com/ingramzhao/Learning/Go/ch9/services"
	"testing"
)

func TestPackage(t *testing.T) {
	v,err := services.GetFibonacci(10)
	if err != nil {
		panic(err)
	}
	t.Log(v)
}