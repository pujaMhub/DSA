def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    leftside=arr[:mid]
    rightside=arr[mid:]

    sortl=mergesort(leftside)
    sortr=mergesort(rightside)

    return merge(sortl,sortr)
def merge(left,right):
    result=[]
    i=j=0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
arr=[4,3,2,1,21,32,12,56,43,78]
sort=mergesort(arr)
print(sort)