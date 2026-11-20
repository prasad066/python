def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=len(arr)-1
    i=0
    for j in range(len(arr)-1):
        if arr[j]<=arr[pivot]:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    arr[pivot],arr[i]=arr[i],arr[pivot]
    left=quick_sort(arr[:i])
    right=quick_sort(arr[i+1:])
    return (left+[arr[i]]+right)
array=[1,1,9,2,8,3,7,4,6,5,5,5]
print(quick_sort(array))