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



if __name__ == "__main__":
    arry = [32,4,60,71,11,23,7]
    # res = bubblesort(arry)
    res = quitsort(arry)
    print(res)
    