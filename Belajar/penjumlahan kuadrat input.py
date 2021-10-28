#jumlah input kuadrat pertama
a = int(input("masukkan total kuadrat ke : "))
d = 0
for i in range (1,a+1):
    b = d
    a = i * i
    c = b + a
    d = c
    print (a)
print ("total = ",d)
