""" 
- 冒泡排序：重复访问要排序的数列，一次比较两个元素，如果它们的顺序错误则交换，否则继续比较交换
- 平均时间复杂度：O(n^2)
    - 最好情况：O(n)
    - 最坏情况：O(n^2)
- 空间复杂度：O(1)
- 排序方式：In-place
- 稳定性：稳定 
"""
def bubblesort(L):
    for i in range(len(L)-1,-1,-1):
        for j in range(i):
            if L[j] > L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]
    return L 

""""
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

"""
def quitsort(L):
    # 结束条件
    if len(L) < 2:
        return L 
    mid = L[0]
    L.remove(mid)
    left,right = [],[]
    for i in L:
        if i <= mid:
            left.append(i)
        else: 
            right.append(i)
    return quitsort(left) + [mid] + quitsort(right)

"""
- 选择排序：选择排序法：即在所有数据中，找到最大元素（最小元素）放到最后一个位置（放到第一个位置）
- 平均时间复杂度：O(n^2)
    - 最好情况：O(n^2)
    - 最坏情况：O(n^2)
- 空间复杂度：O(1)
- 排序方式：In-place
- 稳定性：不稳定
"""
def selectionsort(L):
    for i in range(len(L)-1):
        for j in range(i+1,len(L)):
            if L[i] > L[j]:
                L[i],L[j] = L[j],L[i]
    return L 

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
    # res = bubblesort(arry)
    # res = quitsort(arry)
    # res = selectionsort(arry)
    # res = insertsort(arry)
    # res = shellsort(arry)
    res = mergesort(arry)
    print(res)

"""
- 计数排序：计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数
- 平均时间复杂度：O(n+K)
    - 最好情况：O(n+k)
    - 最坏情况：O(n+K)
- 空间复杂度：O(K)
- 排序方式：Out-place
- 稳定性：稳定

- 堆积排序法：积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子节点的键值或索引总是小于（或者大于）它的父节点。
- 堆排序可以说是一种利用堆的概念来排序的选择排序。分为两种方法：
    - 大顶堆：每个节点的值都大于或等于其子节点的值，在堆排序算法中用于升序排列
    - 小顶堆：每个节点的值都小于或等于其子节点的值，在堆排序算法中用于降序排列

- 平均时间复杂度：O(nlogn)
    - 最好情况：O(nlogn)
    - 最坏情况：O(nlogn)
- 空间复杂度：O(1)
- 排序方式：In-place
- 稳定性：不稳定


- 桶排序：桶排序是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。为了使桶排序更加高效，我们需要做到这两点：
    1. 在额外空间充足的情况下，尽量增大桶的数量
    2. 使用的映射函数能够将输入的 N 个数据均匀的分配到 K 个桶中

- 平均时间复杂度：O(n+K)
    - 最好情况：O(n+k)
    - 最坏情况：O(n^2)
- 空间复杂度：O(n+K)
- 排序方式：Out-place
- 稳定性：稳定

- 基数排序法：
    - 基数排序有两种方法：
    - 这三种排序算法都利用了桶的概念，但对桶的使用方法上有明显差异案例看大家发的：
        1. 基数排序：根据键值的每位数字来分配桶；
        2. 计数排序：每个桶只存储单一键值；
        3. 桶排序：每个桶存储一定范围的数值

- 平均时间复杂度：O(n*K)
    - 最好情况：O(n*k)
    - 最坏情况：O(n*2)
- 空间复杂度：O(n+K)
- 排序方式：Out-place
- 稳定性：稳定
"""