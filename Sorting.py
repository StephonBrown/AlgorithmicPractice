#%%
def HeapSort(arr):
    n = len(arr)
    
array = [3,7,2,1,4]
HeapSort(array)
# %%
def Partition(arr, low, high):
    #The element being pivoted around
    pivot = arr[high]
    #This is the element after the element being focused on in the loop
    i = low - 1

    for j in range(low, high):
        #if the current element is less than the pivot, move it to the lefy
        if(arr[j] < pivot):
            i = i+1
            #Make this swap more pythonic like this arr[j], arr[i] = arr[i], arr[j]
            swap = arr[i]
            arr[i] = arr[j]
            arr[j] = swap

    ##This swap is done to make sure the pivot is placed between number
    # less than and numbers greater than the pivot after going through all numbers
    swap = arr[i + 1]
    arr[i+1] = arr[high]
    arr[high] = swap

    return i + 1
 
def QuickSort(arr, low, high):
    if(low < high):
        par = Partition(arr, low, high)

        QuickSort(arr, low, par - 1)
        QuickSort(arr, par + 1, high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
QuickSort(arr,0,n-1) 
print ("Sorted array is:") 
print(arr)
# %%
