count = 0
def sort(mylist, p, q):
    global count
    x = mylist[p]
    i = p
    for j in range (p+1, q+1):
        if mylist[j]<=x:
            i += 1
            mylist[i], mylist[j] = mylist[j], mylist[i]
        count += 1
        print (count,"=",mylist)
    mylist[p], mylist[i] = mylist[i], mylist[p]
    return i, count

def quickSort(mylist,p,q):
    if p < q:
        r = sort(mylist,p,q)[0]
        quickSort(mylist,p,r-1)
        quickSort(mylist,r+1,q)
    return count

mylist = [20,23,27,21,19,11,4]
quickSort(mylist,0,len(mylist)-1)
print (mylist)
