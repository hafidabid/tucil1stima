def heapPermutation(arr,arrSize):
    if(arrSize==1):
        return arr
    else:
        res = []
        for y in range(arrSize):
            res = res+heapPermutation(arr,arrSize-1)
            if(arrSize%2==1):
                arr[0],arr[arrSize-1] = arr[arrSize-1],arr[0]
            else:
                arr[y],arr[arrSize-1] = arr[arrSize-1],arr[y]

        return res

def pisahkan(arr,n):
    res = []
    temp = []
    count = 0
    for x in arr:
        if count<n:
            temp.append(x)
            count=count+1
        else:
            res.append(temp)
            temp=[]
            temp.append(x)
            count = 1

    res.append(temp)
    return res
