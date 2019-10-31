from math import floor
def merge(first_partition,second_partition):

        # create temporary arrays
        temp = []
        i,j = 0,0 
        # merge the two sequenced together until one is empty
        while i<len(first_partition) and j<len(second_partition):
                if(first_partition[i] <= second_partition[j]):
                        temp.append(first_partition[i])
                        i=i+1
                else:
                        temp.append(second_partition[j])
                        j=j+1
                

        
        temp += first_partition[i:]
        temp += second_partition[j:]

        return temp


def mergeDivider(array):
    
    # Takes in an array ,the index of the first element
    # and last element as parameters to a function

    # checks if the first index is equal to the last index
        if(len(array) <=1):
                return array;
                
        #  get the index of the middle
        mid =  floor((len(array))/2)
        #initialize all the partition
        first_partition = mergeDivider(array[:mid])
        second_partition = mergeDivider(array[mid:])

        # mergeDivider the first part
        # for merging  the partition
        return merge(first_partition,second_partition)
    
def mergeSort(array):
    return mergeDivider(array)


r = mergeSort([1,3,4,2,5,4,6,7,8,6,12]);

print(r);