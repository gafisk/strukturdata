def mergeSort(mylist):
    print("Divide", mylist)
    if len(mylist) > 1:
        mid = len(mylist) // 2
        left_half = mylist[:mid]
        right_half = mylist[mid:]
        mergeSort(left_half)
        mergeSort(right_half)
        i = 0
        j = 0
        k = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                mylist[k] = left_half[i]
                i += 1
            else:
                mylist[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            mylist[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            mylist[k] = right_half[j]
            j += 1
            k += 1
        print("Merging", mylist)

mylist = [5,2,4,1,6,8,3]
mergeSort(mylist)
