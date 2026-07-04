def insertion(arr):
    n=len(arr)
    for i in range(1,n):
        insert_index=i
        current = arr[i]
        for j in range(i-1,-1,-1):
            if arr[j]>current:
                arr[j+1]=arr[j]
                insert_index=j
            else:
                break
        arr[insert_index]=current
    return arr
arr= [5,4,2,3,1]
print(insertion(arr))