"""
- 插入排序法：将数组中的元素逐一与已排序好的数据进行比较
- 平均时间复杂度：O(n^2)
    - 最好情况：O(n)
    - 最坏情况：O(n^2)
- 空间复杂度：O(1)
- 排序方式：In-place
- 稳定性：稳定
- 优化算法：拆半插入
"""
def insertsort(arr):
    for i in range(1,len(arr)):
        # 暂时存放数据
        current = arr[i]
        preIndex = i - 1
        while preIndex >= 0 and current < arr[preIndex]:
            # 就把所有元素往后推一个位置
            arr[preIndex + 1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex + 1] = current
    return arr
if __name__ == "__main__":
    arry = [32,4,60,71,11,23,7]
    res = insertsort(arry)
    print(res)