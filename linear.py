def linear(arr,k):
    for i in range(len(arr)):
        if arr[i]==k:
            return i
    return -1
arr=[34,543,133,10]
k=10
result=linear(arr,k)
print(linear(arr,k))