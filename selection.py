def selection(arr):
    n=len(arr)
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini = j
        arr[i],arr[mini]=arr[mini],arr[i]
    return arr
arr=[54,65,2,1,23]
print(selection(arr))