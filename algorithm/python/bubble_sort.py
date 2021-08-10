def bubbleSort(arr):

    print(len(arr))

    for i in range(len(arr)):
        print(i)
        
        for j in range(0, len(arr)-i-1):

            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    print(arr)  
#   print(arr(i))

arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])