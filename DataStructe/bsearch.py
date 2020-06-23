def bsearch(L,n,target):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low+high) // 2
        if L[mid] == target:
            return mid 
        elif (L[mid]) < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    arry = [4,20,21,50,60,71]
    
    print(bsearch(arry,len(arry),71))