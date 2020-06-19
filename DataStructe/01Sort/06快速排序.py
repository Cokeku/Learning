"""
- 快速排序：使用“分而治之”的方式，先找到一个中间值，并按此中间值将所有打算排序的数据分为两个部分：
    1.小于中间值的数据放在左边
    2.大于中间值的数据放在右边
    3.再以同样的方式处理左右两边的数据

- 平均时间复杂度：O(nlogn)
    - 最好情况：O(nlogn)
    - 最坏情况：O(n^2)
- 空间复杂度：O(logn)
- 排序方式：In-place
- 稳定性：不稳定


递推公式：
quick_sort(p…r) = quick_sort(p…q-1) + quick_sort(q+1… r)

终止条件：
p >= r

伪代码：
// 快速排序，A是数组，n表示数组的大小
quick_sort(A, n) {
  quick_sort_c(A, 0, n-1)
}
// 快速排序递归函数，p,r为下标
quick_sort_c(A, p, r) {
  if p >= r then return
  
  q = partition(A, p, r) // 获取分区点
  quick_sort_c(A, p, q-1)
  quick_sort_c(A, q+1, r)
}
"""
def quitsort(L,start,end):
    if not L or start >= end : return 
    left, right, povit = start, end, L[start]
    while left < right:
        while left < right and L[right] >= povit:
            right -= 1
        L[left] = L[right]

        while left < right and L[left] < povit:
            left += 1
        L[right] = L[left]

    L[left] = povit
    quitsort(L,start,left-1)
    quitsort(L,left+1,end)

if __name__ == "__main__":
    arry = [32,4,60,71,11,23,7]
    quitsort(arry,0,len(arry)-1)
    print(arry)