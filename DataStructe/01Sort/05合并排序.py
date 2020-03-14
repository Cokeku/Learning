"""
- 合并排序法：针对已排序好的两个或两个以上的数列，通过合并的方式将其组合成一个大的且已排好序的数列
- 平均时间复杂度：O(nlogn)
    - 最好情况：O(nlogn)
    - 最坏情况：O(nlogn)
- 空间复杂度：O(n)
- 排序方式：Out-place
- 稳定性：稳定
"""
# 定义合并排序函数
def mergesort(arr):
    if(len(arr)<2):
        return arr
    middle = len(arr)//2
    left, right = arr[0:middle], arr[middle:]
    # 递归
    return merge(mergesort(left), mergesort(right))

# 定义合并函数
def merge(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result
if __name__ == "__main__":
    arry = [32,4,60,71,11,23,7]
    res = mergesort(arry)
    print(res)