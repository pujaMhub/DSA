def bubble(arr):
    n = len(arr)

    for i in range(n-1):
        swap = False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap = True

    return arr
arr=[2,34,1,98,64,9]
print(bubble(arr))

# bubble sort
def bub(arr):
    n=len(arr)

    for i in range(n-1):
        swap=False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap = True
        if not swap:
            break
    return arr
arr=[5,3,2,4,2]
print(bub(arr))
