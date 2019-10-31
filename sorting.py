def  selectionSort(list):
    for i in range(len(list)-1):
        min = i
        for j in range(i+1,len(list)):
            if list[j] < list[min]:
                min = j
        if i != min:
            list[i],list[min] = list[min],list[i]
    return list


def bubbleSort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(len(list)-i):
            if list[j] < list[i]:
                list[j+1],list[i] = list[i],list[j+1]
            print(list)
    return list

def insertionSort(list):
    for i in range(1,len(list)):
        temp =  list[i]
        j = i-1
        while(j>=0 and list[j]>temp):
            list[j+1] = list[j]
            j = j-1
        list[j+1] = temp
m = [2,4,5,2,6,8,75,83,0]
x = bubbleSort(m)
print(x)
