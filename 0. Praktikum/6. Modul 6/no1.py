def search(listdata,key):
    founded=[]
    i=0
    cek=listdata
    temp=False
    while i<len(listdata) and key in cek:
        if listdata[i] == key:
            founded.append(i)
            cek[i]=key-1
            temp=True
        i+= 1
    if temp:
        return founded, i
    else:
        return ('data tidak ditemukan'),i

listku = [1,5,9,8,1,5,10,26,5,12]
[hasil,count]=search(listku,5)
print("Posisi data=",hasil)
print("Jumlah iterasi=",count)
