def binSearch(listdata,key):
    found=False
    founded=[]
    i=0
    last=len(listdata)-1
    count=0
    while i<=last and not(found):
        mid=(i+last)//2
        if listdata[mid]==key:
            founded.append(mid)
            if listdata[mid-1]==key:
                temp = mid
                while listdata[temp-1]==key:
                    temp-=1
                    founded.append(temp)
                found=True
            if listdata[mid+1]==key:
                temp = mid
                while listdata[temp+1]==key:
                    temp+=1
                    founded.append(temp)
                found=True
            found = True
        elif key>listdata[mid]:
            i=mid+1
        else:
            last=mid-1
        count+=1
    if found:
        return founded, count
    else:
        return ('Data tidak ada'),count

    
listku = [1,1,5,5,5,8,9,10,12,26]
[hasil,count] = binSearch(listku,1)
print("Posisi data=",hasil)
print("Jumlah iterasi=",count)
