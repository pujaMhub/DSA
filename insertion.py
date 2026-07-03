def insert(arr):
    n=len(arr)
    for i in range(1,n):
        insertindex=i
        current=arr[i]
        for j in range(i-1,-1,-1):
            if arr[j]>current:
                arr[j+1]=arr[j]
                insertindex=j
            else:
                break
        arr[insertindex]=current
    return arr
arr=[4,53,2,34,1]
print(insert(arr))

def insert(arr):
    n=len(arr)

    for i in range(1,n):
        insertindex=i
        current = arr[i]
        for j in range(i-1,-1,-1):
            if arr[j]>current:
                arr[j+1]=arr[j]
                insertindex=j
            else:
                break
        arr[insertindex]=current
    return arr
arr=[3,4,3,1,3,23]
print(insert(arr))
