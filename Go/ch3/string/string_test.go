package string_test

import "testing"

func TestStrings(t *testing.T){
	s1 := "中hello"
	t.Logf("%s len %d",s1,len(s1))  // string底层是一个bytes类型的slice
	
	s2 := []rune(s1)	// 类型转化成rune utf-8: 3-4个bytes
	t.Logf("unicode %c len %d",s2[1],len(s2))
	t.Logf("utf-8 %x",s1)
	for _,v := range s1 {
		t.Logf("%x",v)
	}
}

func TestStringToRune(t *testing.T) {
	s := "中华人民共和国hello"
	for _, c := range s {
		t.Logf("%[1]c %[1]d", c,)  // unicode表示
	}
}