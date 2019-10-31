def bubbleSort(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1]= arr[j+1],arr[j]
    return arr

print(bubbleSort([1,4,3,5,0,67,3,8]))