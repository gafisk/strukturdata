def check(sortedList):
    if (sortedList == sorted(sortedList)):
        return True
    else:
        return False


def bubbleSort(listData):
    print('Data yang akan diurutkan : ', listData)
    count = 0
    outIter = len(listData)-1
    if check(listData) == False:
        while outIter > 0:
            count = count+1
            print('Iterasi ke-', count, ':')
            for i in range(outIter):
                if listData[i] < listData[i+1]:
                    temp = listData[i]
                    listData[i] = listData[i+1]
                    listData[i+1] = temp
                print(listData)

            if check(listData) == True:
                outIter = 0
            else:
                outIter -= 1
        print('Data urut-', listData)
    else:
        print("Data sudah urut-", listData)


isi = []
jumlah = int(input("Masukkan total data : "))
for i in range(1,jumlah+1):
    data = int(input("Masukkan data ke %d - " % i))
    isi.append(data)
    
bubbleSort(isi)
