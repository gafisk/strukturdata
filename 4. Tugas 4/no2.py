def bubblesort(data):
    c = 0
    i = len(data)-1
    while i > 0:
        print("Iterasi ke-"+str(c+1))
        c+=1
        h=1
        s1=0
        s2=0
        print("Dari kiri ke kanan")
        for j in range (i):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
            else:
                s1 += 1
            print(f"[{j+1}]: {data}")
        print("Dari kanan ke kiri")
        
        for k in range(i,0,-1):
            if data[k] < data[k-1]:
                data[k],data[k-1] = data[k-1],data[k]
            else:
                s2 += 1
            print(f"[{h}]: {data}")
            h+=1

        if s1 == i:
            i = 0
        else:
            i -= 1
        print()
    return data

hasil = []
jumlah = int(input("Masukkan Jumlah Data : "))
for i in range (1,jumlah + 1):
    data = int(input("Masukkan data ke %d = " % i))
    hasil.append(data)
print("")
print("data = ",hasil)
print("")
print("data terurut:",bubblesort(hasil))
