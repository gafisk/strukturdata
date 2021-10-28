def reminderFunction (data,num) :
    return data%num

def createHashTable(num) :
    return [[None] for i in range(num)]

def chaining (data,table) :
    for i in range (len(data)) :
        ind = reminderFunction(data[i], len(table))
        if table[ind][0] == None:
            table[ind][0] = data[i]
        else :
            table[ind].append(data[i])
            
def searchHash(data,table) :
    hashVal = reminderFunction(data, len(table))
    if table[hashVal] != None :
        cek = False
        for i in range(len(table[hashVal])):
            if data == table[hashVal][i]:
                print("(\'data berada di slot ke-\' {},\' dan index ke-\', {})".format(hashVal, i))
                cek = True
        if cek == False :
            print("False")
    else :
        print("False")

#54 [11]
#hasval = 10
#if table[10][0] 

slot = reminderFunction(55,10)
print(slot)
hashtable = createHashTable(11)
print(hashtable)
a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
chaining(a, hashtable)
print(hashtable)
searchHash(66, hashtable)
searchHash(54, hashtable)
searchHash(20, hashtable)
searchHash(55, hashtable)
searchHash(100, hashtable)
