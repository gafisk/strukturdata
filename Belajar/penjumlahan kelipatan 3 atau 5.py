#jumlah dari kelipatan 3 atau 5
n = int(input("Masukkan Angka = "))
u = []
for i in range (1,n):
    if i % 3 == 0:
        u.append(i)
    elif i % 5 == 0:
        u.append(i)
jumlah = sum(u)
print (u, "=", jumlah)
"""
a = 0
b = 0
d = 0
for i in range (1, n+1):
    if i % 3 == 0:
        b = i
    elif i % 5 == 0:
        d = i
    f = a
    g = b + i
    a = g
print (b,"dan", d)
print (a)"""
