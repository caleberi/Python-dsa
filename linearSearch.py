def LinearSearch(arr,target):
    for i in range(len(arr)):
        if(arr[i] == target):
            return True
    return False



v = LinearSearch([2,3,4,5,23,6,44],4)
print(v)