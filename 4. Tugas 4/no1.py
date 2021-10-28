def cek(listData):
    s = 0
    for i in range (len(listData)-1):
        if listData[i] < listData[i+1]:
            s += 1
    if s == len(listData)-1:
        return True
    else:
        return False

def bubbleSort(listData):
    print('Data yang akan diurutkan : ', listData)
    count = 0
    outIter = len(listData)-1
    if not cek(listData):
        while outIter > 0:
            s = 0
            count = count+1
            print('Iterasi ke-', count, ':')
            for i in range(outIter):
                if listData[i] > listData[i+1]:
                    temp = listData[i]
                    listData[i] = listData[i+1]
                    listData[i+1] = temp
                else:
                    s += 1

                print(listData)

            if s == outIter:
                outIter = 0
            else:
                outIter -= 1
        print('Data urut-', listData)
    else:
        print("data sudah terurut")


hasil = []
jumlah = int(input("Masukkan Jumlah Data : "))
for i in range (1,jumlah + 1):
    data = int(input("Masukkan data ke %d = " % i))
    hasil.append(data)
    
bubbleSort(hasil)

