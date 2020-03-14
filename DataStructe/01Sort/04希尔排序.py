"""
-希尔排序法：将数据区分成特定间隔的几个小区块，以插入排序法排完区块内的数据后再渐渐减少间隔
- 平均时间复杂度：O(nlogn)
    - 最好情况：O(nlog^2n)
    - 最坏情况：O(nlog^2n)
- 空间复杂度：O(1)
- 排序方式：In-place
- 稳定性：不稳定
"""
def shellsort(arr):
    jmp = len(arr)//2
    while jmp != 0:
        for i in range(jmp,len(arr)):
            tmp = arr[i]
            # 用j来定位比较的元素
            j = i - jmp
            # 插入排序
            while j >= 0 and arr[j] > tmp:
                arr[j+jmp] = arr[j]
                j = j - jmp
            arr[jmp+j] = tmp
        jmp = jmp//2
    return arr

if __name__ == "__main__":
    arry = [32,4,60,71,11,23,7]
    res = shellsort(arry)
    print(res)