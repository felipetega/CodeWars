def dirReduc(array):
    hashMap = {"NORTH":"SOUTH","SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}
    result = []
    for i in array:
        if result and hashMap[i] == result[-1]:
            result.pop()
        else:
            result.append(i)
    return result