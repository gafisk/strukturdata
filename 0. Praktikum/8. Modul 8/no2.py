perbandingan = 0
pergeseran = 0
def mergeSort(arr):
    global perbandingan,pergeseran
    if len(arr) > 1:
        print("splitting",arr," = ",end="")
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]       
        print(left,",",right)
        mergeSort(left)
        mergeSort(right)
        i,j,k = 0,0,0
        print("merging",left," and ",right," = ",end="")
        while i < len(left) and j < len(right):
            perbandingan += 1 
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
                pergeseran += 1
            else:
                arr[k] = right[j]
                j += 1
                pergeseran += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            pergeseran += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            pergeseran += 1
        print(arr,"\n")
    else:
        print("no spliting = ",arr)

a = [5,3,2,4,1,7,6,8]
print("Sebelum di urutkan : ",a)
mergeSort(a)
print("Banyak Pergeseran = ",pergeseran)
print("Banyak Perbandingan = ",perbandingan)
print("Sesudah di urutkan : ",a)

iteration = 1
perbandingan = 0
pergeseran = 0
def partition(arr,p,q):
    global iteration,perbandingan,pergeseran
    pivot = arr[p]
    i = p
    print("iterasi ke-",iteration)
    print("Pivot =",pivot)
    for j in range(p+1,q+1):
        perbandingan += 1
        print(f"pivot >= {arr[j]} ? {pivot >= arr[j]}",end="")
        if pivot >= arr[j]:
            pergeseran += 1
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
        print(f", \tData = {arr}")
    arr[i],arr[p] = arr[p],arr[i]
    print("Data Akhir = ",arr)
    iteration += 1
    return i

def Quicksort(arr,p,q):
    if p < q:
        r = partition(arr,p,q)
        Quicksort(arr, p, r-1)
        Quicksort(arr, r+1, q)

a=[37,83,10,1,45,25,12,90,54]
print("Sebelum di urutkan : ",a)
Quicksort(a,0,len(a)-1)
print("Banyak Pergeseran = ",pergeseran)
print("Banyak Perbandingan = ",perbandingan)
print("Sesudah di urutkan : ",a)


