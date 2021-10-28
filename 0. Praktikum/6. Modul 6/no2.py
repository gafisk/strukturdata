def search(data,key):
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
        return found, i
    else:
        return "data tidak ada", i

listku = [1,1,5,5,5,8,9,10,12,26]
[hasil,count]=search(listku,5)
print("Posisi data= ",hasil)
print("Jumlah iterasi= ",count)
