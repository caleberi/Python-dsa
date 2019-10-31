def binarySearchInterative(data,target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low+high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid -1
        else:
            high = mid + 1
    return False


def BinarySearch(arr,target,low,high):
    if low > high:
        return False
    else:
        mid = (low+high)//2
        if target == arr[mid]:
            return True
        elif target < arr[mid]:
            return BinarySearch(arr,target,low,mid-1)
        else:
            return BinarySearch(arr,target,mid+1,high)
    return False
arr = [1,2,5,4,7,5,8,2,4,7]




print(BinarySearch(arr,5,0,len(arr)-1))
print(arr)
