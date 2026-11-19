def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=len(arr)-1
    i=0
    for j in range(len(arr)-1):
        if arr[j]<=arr[pivot]:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    arr[i],arr[-1]=arr[-1],arr[i]
    left=quick_sort(arr[:i])
    right=quick_sort(arr[i+1:])
    return (left+[arr[i]]+right)
ar=[8, 1, 9, 5, 6, 3, 7, 4, 2, 5 ]
p=len(ar)-1
print(quick_sort(ar))


