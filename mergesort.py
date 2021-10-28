def mergesort(listku):
    print("devide", listku)
    if len(listku) > 1:
        mid = len(listku) // 2
        left_half = listku[:mid]
        right_half = listku[mid:]
        mergesort(left_half)
        mergesort(right_half)
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:
                listku[k] = left_half[i]
                i += 1
            else:
                listku[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            listku[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            listku[k] = right_half[j]
            j += 1
            k += 1
        print ("Marging", listku)

listku = [26,30,12,48,90,15]
counter = mergesort(listku)
print(listku)
