def bin(arr,tar):
    left=0
    right=len(arr)-1

    while left<right:
        mid = (left+right)//2

        if arr[mid]==tar:
            return mid
        if arr[mid]<tar:
            left= mid+1
        else:
            right=mid-1
    return -1
arr=[3,4,2,1,6,5,7,30]
tar=5
result=bin(arr,tar)
print(result)