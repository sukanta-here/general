def insertionSort(arr):

    for i in range(1,len(arr)):

        key = arr[i]
        j = i-1

        while key < arr[j] and j >=0:

            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key        

arr = [64, 34, 25, 12, 22, 11, 90]
print (arr) 
insertionSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])