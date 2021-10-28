def insertionSort(mylist):
    for i in range(1,len(mylist)):
        key = mylist[i]
        j = i-1
        while j>=0 and key<=mylist[j]:
            mylist[j+1]=mylist[j]
            j-=1
        mylist[j+1]=key
    return mylist

def OrderedSeqSearch(data,key):
    i = 0
    stop = False
    found  = []
    while not stop and i<len(data):
        
        if data[i] == key:
            found.append(i)
        elif data[i] > key:
            stop = True
        i += 1
    if found != []:
        return f"{key} di indeks : {found}, iterasi ke: {i}"
    else:
        return f"{key} tidak ditemukan, iterasi ke: {i}"


n = [9,12,5,3,15,18,14]

insertionSort(n)
print("Data =",n,"\n")
print(OrderedSeqSearch(n,12))
