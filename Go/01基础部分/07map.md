## map

map是一种无序的基于`key-value`的数据结构，Go语言中的map是引用类型，必须初始化才能使用

定义：`map[KeyType]ValueType`

map类型的变量默认初始值为nil，需要使用make()函数来分配内存：`make(`map[KeyType]ValueType`,cap)`

### 1.基本使用

`demo1`:

```go
func main() {
	scoreMap := make(map[string]int, 8)
	scoreMap["张三"] = 90
	scoreMap["小明"] = 100
	fmt.Println(scoreMap)
	fmt.Println(scoreMap["小明"])
	fmt.Printf("type of a:%T\n", scoreMap)
}

// 输出结构：
map[小明:100 张三:90]
100
type of a:map[string]int
```

`demo2`：在声明的时候填充元素

```go
func main() {
	userInfo := map[string]string{
		"username": "沙河小王子",
		"password": "123456",
	}
	fmt.Println(userInfo) 
}
```



### 2.判断某个键是否存在

格式：`value,ok := map[key]`

```go
func main() {
	scoreMap := make(map[string]int)
	scoreMap["张三"] = 90
	scoreMap["小明"] = 100
	// 如果key存在ok为true,v为对应的值；不存在ok为false,v为值类型的零值
	v, ok := scoreMap["张三"]
	if ok {
		fmt.Println(v)
	} else {
		fmt.Println("查无此人")
	}
}
```



### 3.map的遍历

Go语言中是使用`for range`遍历map

```go
func main() {
	scoreMap := make(map[string]int)
	scoreMap["张三"] = 90
	scoreMap["小明"] = 100
	scoreMap["娜扎"] = 60
	for k, v := range scoreMap {
		fmt.Println(k, v)
	}
    // 如果只想遍历key的时候
    for k, := range scoreMap{
        fmt.Prinln(k)
    }
}

```



### 4.使用delete()函数删除键值对

格式：`delete(map,key) map: 表示要删除键值对的map；key：表示要删除的键值对的键`

```go
func main() {
	scoreMap := make(map[string]int)
	scoreMap["张三"] = 90
	scoreMap["小明"] = 100
    delete(scoreMap,"小明")
	for k, v := range scoreMap {
		fmt.Println(k, v)
	}
}
```



### 5. 按照指定顺序遍历map

`demo`: 取出map中的所有key存放在切片keys中，然后对切片进行排序，然后按照排序后的key遍历map

```go
func main() {
	rand.Seed(time.Now().UnixNano()) //初始化随机数种子

	var scoreMap = make(map[string]int, 200)

	for i := 0; i < 100; i++ {
		key := fmt.Sprintf("stu%02d", i) //生成stu开头的字符串
		value := rand.Intn(100)          //生成0~99的随机整数
		scoreMap[key] = value
	}
	//取出map中的所有key存入切片keys
	var keys = make([]string, 0, 200)
	for key := range scoreMap {
		keys = append(keys, key)
	}
	//对切片进行排序
	sort.Strings(keys)
	//按照排序后的key遍历map
	for _, key := range keys {
		fmt.Println(key, scoreMap[key])
	}
}
```



### 6.元素为map类型的切片

`demo`: 列表中的元素为字典

```go
func main() {
	var mapSlice = make([]map[string]string, 3)
	for index, value := range mapSlice {
		fmt.Printf("index:%d value:%v\n", index, value)
	}
	fmt.Println("after init")
	// 对切片中的map元素进行初始化
	mapSlice[0] = make(map[string]string, 10)
	mapSlice[0]["name"] = "小王子"
	mapSlice[0]["password"] = "123456"
	mapSlice[0]["address"] = "沙河"
	for index, value := range mapSlice {
		fmt.Printf("index:%d value:%v\n", index, value)
	}
}
```



### 7.值为切片类型的map

`demo`: 字典中的值对应是列表

```go
func main() {
	var sliceMap = make(map[string][]string, 3)
	fmt.Println(sliceMap)
	fmt.Println("after init")
	key := "中国"
	value, ok := sliceMap[key]
	if !ok {
		value = make([]string, 0, 2)
	}
	value = append(value, "北京", "上海")
	sliceMap[key] = value
	fmt.Println(sliceMap)
}
```

### 8. 练习

`demo1`: 统计单词出现次数

```go
func main() {
	s1 := "how do you do"
	map1 := make(map[string]int,10)
   	// 默认以空格字符为分割成切片
	c := strings.Fields(s1)
	for _,v := range c {
		map1[v]++
	}
	fmt.Println(c)
	fmt.Println(map1)
}
```

`demo2`: 输出结果

```go
func main() {
	type Map map[string][]int
	m := make(Map)
	s := []int{1, 2}
	s = append(s, 3)
	fmt.Printf("%+v\n", s)
	m["q1mi"] = s
    // 这里在切片中删除元素的时候，是将删除的元素后面的向前复制，切片长度也会减少
	s = append(s[:1], s[2:]...)
	fmt.Printf("%+v \n长度：%d 容量：%d\n", s,len(s),cap(s))
    // 但是map[k]对应的切片长度没有改变
	fmt.Printf("%+v\n", m["q1mi"])
}
```

