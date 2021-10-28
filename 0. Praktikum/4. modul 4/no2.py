def ascending(listku):
    temp = 0
    x = len(listku) // 2
    y = len(listku)-1
    for i in range(x):
        temp+=1
        print(f"Iterasi ke- {temp} :")
        c = i
        d = y
        for j in range(i+1,len(listku)):
            if listku[c] > listku[j]:
                c = j
        listku[c], listku[i] = listku[i], listku[c]
        print("urut data minimal : ", (listku))
        for k in range(y-1,-1,-1):
            if listku[d] < listku[k]:
                d = k
        listku[d], listku[y] = listku[y], listku[d]
        print("urut data maksimal : ", (listku))
        y -= 1

    return listku


data = [10,2,5,8,1,20,7,12,4]
print("Algoritma Modifikasi Selection Sort")
print("Data awal= ", data)
print("Data urut= ",ascending(data))

