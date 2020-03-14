"""
- 选择排序法：选择排序法：即在所有数据中，找到最大元素（最小元素）放到最后一个位置（放到第一个位置）
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
if __name__ == "__main__":
    arry = [32,4,60,71,11,23,7]
    res = selectionsort(arry)
    print(res)