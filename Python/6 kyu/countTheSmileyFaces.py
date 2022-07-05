def count_smileys(arr):
    dict={";)":0,";D":0,":)":0,":D":0,":~D":0,":~)":0,":-D":0,":-)":0,";~D":0,";~)":0,";-D":0,";-)":0}
    res=[]
    if arr==[]:
        return 0
    for i in range(0,len(arr)):
        if arr[i] in dict:
            dict[arr[i]]+=1
    return sum(map(int, dict.values()))
    ##return sum(int(x) for x in dict.values())