def unique_in_order(arr):
    res=[]
    if len(arr)==0:
        return []
    else:
        for i in range(0,len(arr)):
            if i+1<len(arr):
                if arr[i] !=arr[i+1]:
                    res.append(arr[i])
        res.append(arr[-1])
    return res