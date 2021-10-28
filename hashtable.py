def create(num):
    temp = []
    for i in range (num):
        temp.append(None)
    return temp

def reminder(data,num):
    return data%num

def putdata(data,table):
    for i in range(len(data)):
        ind = reminder(data[i], len(table))
        if table[ind] == None:
            table[ind] = []
        table[ind].append(data[i])
    return table

def search(data,table):
    i = 0
    found = False
    while i < len(table) and not found:
        if table[i] != None and data in table[i]:
            ind = table[i].index(data)
            found = True
        else:
            i += 1
    if found:
        return i, ind, True
    else:
        return False

data = [2,1,29,7,4,5,20,40,12,3]
slot = 10
hashtable = create(slot)
hashtable = putdata(data,hashtable)
datacari = 12
found = search(datacari, hashtable)
print(hashtable)

if not found:
    print(f"{datacari} Tidak ada dalam hasttable")
else:
    print(f"{datacari} berada di slot {found[0]} di indeks ke - {found[1]}")
