def createHashTable(num):
    temp = []
    for i in range(num):
        temp.append(None)
    return temp
 
def reminderFunction(data,num):
    return data%num
 
def putData(data,table):
    for i in range(len(data)):
        ind = reminderFunction(data[i],len(table))
        if table[ind] == None:
            table[ind] = []
        table[ind].append(data[i])
    return table
 
def searchHash(data,table):
    i = 0
    found = False
    while i < len(table) and not found:
        if table[i] != None and data in table[i]:
            ind  = table[i].index(data)
            found = True
        else:
            i += 1
    if found:
        return i, ind, True
    else:
        return False
 
data = [2,1,29,7,18,9,99,10,20,12]
slot = 10
HashTable = createHashTable(slot)
HashTable = putData(data,HashTable)
datacari = 90
found = searchHash(datacari,HashTable)
print(HashTable)
 
if not found:
    print(f"{datacari} Tidak ada dalam hash table")
else:
    print(f"{datacari} berada di slot {found[0]} di indeks ke - {found[1]}")
