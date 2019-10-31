def  quickSort(arr):
    quick_sorter(arr,0,len(arr)-1)


def quick_sorter(arr,low,high):
    if low < high:
        p = partition(arr,low,high)
        quick_sorter(arr,low,p-1)
        quick_sorter(arr,p+1,high)

def pivot(arr,low,high):
    mid = (high+low)//2
    pivot = high
    if arr[low] < arr[high]:
        if arr[mid] < arr[high]:
            pivot = mid
    elif arr[low] < arr[high]:
        pivot = low
    return pivot


def partition(arr,low,high):
    pivotIdx = pivot(arr,low,high)
    pivotValue =arr[pivotIdx]
    arr[pivotIdx],arr[low] = arr[low],arr[pivotIdx]
    border = low

    for i in range(low,high+1):
        if arr[i] < pivotValue:
            border += 1
            arr[i],arr[border] = arr[border] , arr[i]
    arr[low],arr[border] = arr[border] ,arr[low]

    return (border)
