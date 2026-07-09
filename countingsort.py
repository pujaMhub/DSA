def counting(arr):
    if not arr:
        return arr
    maxval=max(arr)
    count = [0]*(maxval+1)

    for num in arr:
        count[num] +=1

    arr[:]=[]
    for num,freq in enumerate(count):
        arr.extend([num]*freq)
    return arr
arr=[4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
sorted=counting(arr)
print(sorted)