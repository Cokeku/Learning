"""
字节跳动笔试第1题

第一行输入：N
第N行输入：模块类型 模块文件

输出：模块文件 模块类型1 模块类型2....
"""
import sys
map1 = {}
for line in sys.stdin:
    a = line.split()
    if len(a) == 1:
        N = int(a[0])
    else:
        print(a[1],type(a[1]))
        if not a[1] in map1:
            map1[a[1]] = []
        print(map1[a[1]])
        map1[a[1]].append(a[0])
        N -= 1
       
    while N == 0:
        for k,v in map1.items():
             print(k,v)
        sys.exit(0)