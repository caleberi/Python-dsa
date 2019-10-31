#sorts a virtual subsquence in ascending order using merge sort

def mergeDivider(array,left,right):
    # the elements that comprise the virtual array are indicated
    # by the range [first,....,last]. tmp is the temporry storage used in
    # in merging phase of the mergesort alogrithm
    #check the base case: the virtual array contains a single item
        if left<right:
            #computes the middle index of the virtual array
            mid =  (left+ (right - 1 ))//2
            #split the sequence and perform the recursive step
            mergeDivider(array,left,mid)
            mergeDivider(array,mid+1,right)
            #merge the splitted array
            merge(array,left,mid+1,right)

# merge takes in two sorted array  [left,...,right) [right,...,end) as parameter
# merge  those sorted arrays into one array
# return one sorted array
def merge(array,left,mid,right):
    # initalize two subsquences together until one is empty
    a = mid - left + 1
    b = right-mid
    # create temp arrays
    l = [0]*(a)
    r = [0]*(b)
    
    # merge the two sequenced together until one is empty
    for i in range(0,a):
        l[i]= array[left+i] 

    for j in range(0,b):
        r[j]= array[mid+1+j] 

    # merge the temp arrays back
    i=0
    j=0
    k=left

    while i < a and j < b:
        if l[i] <= r[j]:
            array[k] = l[i]
            i+=1
        else:
            array[k] = l[j]
            j+=1 
        k+=1

    #if the left contain left divison of the  array ,append them to the array
    while i < a :
        array[k] = l[i]
        i+=1
        k+=1
    
    #if the left contain right divison of the  array ,append them to the array
    while j < b :
        array[k] = r[j]
        j+=1
        k+=1


# sort an array  or list in ascending order
def mergeSort(array):
    n = len(array)
    mergeDivider(array,0,n-1)


arr = [1,3,4,2,5,4,6,7,8,6,12]

mergeSort(arr);



print(arr)
    



