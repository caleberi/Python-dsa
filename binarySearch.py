def binarySearch(list,target,length):
    low = 0
    high = length -1

    while low <= high:
        mid = (low+high) // 2
        if target < list[mid]:
            high = mid-1 #left half
        elif target > list[mid]:
            low = mid+1  #right half
        else:
            return mid
    return -1


list  = [1,2,3,4,5,6,7,8]
print(binarySearch(list,5,len(list)))
