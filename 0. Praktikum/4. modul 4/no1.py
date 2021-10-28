def ganjilgenap(listku):
    for i in range(len(listku)):
        if i % 2 == 0:
            print("Genap-Ganjil sorting")
            for j in range(0,len(listku)-1,2):
                if listku[j] > listku[j+1]:
                    listku[j], listku[j+1] = listku[j+1], listku[j]
        else:
            print("Ganjil-Genap sorting")
            for j in range(1,len(listku)-1,2):
                if listku[j] > listku[j+1]:
                    listku[j], listku[j+1] = listku[j+1], listku[j]
        
        print(listku)
    
    return listku

listku = [13,12,10,8,7,5,11,2]
print("Data=",listku)
print(f"{ganjilgenap(listku)}")
