def partitionAsccending(arr,p,q):
    pivot = arr[p]
    i = p
    for j in range(p+1,q+1):
        if pivot >= arr[j]:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i],arr[p] = arr[p],arr[i]
    return i

def partitionDesccending(arr,p,q):
    pivot = arr[p]
    i = p
    for j in range(p+1,q+1):
        if pivot <= arr[j]:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i],arr[p] = arr[p],arr[i]
    return i

def mergeSortAsccending(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSortAsccending(left)
        mergeSortAsccending(right)
        i,j,k = 0,0,0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def mergeSortDesccending(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSortDesccending(left)
        mergeSortDesccending(right)
        i,j,k = 0,0,0

        while i < len(left) and j < len(right):

            if left[i] > right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

while True:
    print("pilih cara pengurutan :")
    print("1. QuickSort")
    print("2. MergeSort")
    pil = int(input("Masukan pilihan : "))

    print("tipe pengurutan ?")
    print("1. Asccending")
    print("2. Desccending")
    node = int(input("Masukan pilihan : "))

    inp = input("Masukan Data [1,2,3,4,5] : ")
    data = inp.split(",")
    data = [int(i) for i in data]

    if pil == 1:
        if node == 1:
            def Quicksort(arr,p,q):
                if p < q:
                    r = partitionAsccending(arr,p,q)
                    Quicksort(arr, p, r-1)
                    Quicksort(arr, r+1, q)
            Quicksort(data,0,len(data)-1)
        else:
            def Quicksort(arr,p,q):
                if p < q:
                    r = partitionDesccending(arr,p,q)
                    Quicksort(arr, p, r-1)
                    Quicksort(arr, r+1, q)
            Quicksort(data,0,len(data)-1)
    else:
        if node == 1:
            mergeSortAsccending(data)
        else:
            mergeSortDesccending(data)
    print("Hasil  : ",data)
    tanya = input("Lagi[y/n]?  ")
    if tanya == "n":
        print("program selesai")
        break

