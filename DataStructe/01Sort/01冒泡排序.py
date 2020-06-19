""" 
- 冒泡排序法：重复访问要排序的数列，一次比较两个元素，如果它们的顺序错误则交换，否则继续比较交换
- 平均时间复杂度：O(n^2)
    - 最好情况：O(n)
    - 最坏情况：O(n^2)
- 空间复杂度：O(1)
- 排序方式：In-place
- 稳定性：稳定 
"""
def bubblesort(L):
    for i in range(len(L)):
        flag = False
        for j in range(len(L)-i-1):
            if L[j] > L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]
                flag = True 
        if not flag: break 

if __name__ == "__main__":
    arry = [32,4,60,71,11,23,7]
    bubblesort(arry)
    print(arry)