def counting(A,k):
    C=[]
    B=[]
    count = 0
    for i in range(k+1):
        C.append(0)
    for j in range(len(A)):
        C[A[j]] = C[A[j]]+1
        B.append(0)
    for i in range(1,k+1):
        C[i]= C[i]+C[i-1]
    for j in range (len(A)-1,-1,-1):
        B[C[A[j]]-1] = A[j]
        C[A[j]]=C[A[j]]-1
        print(B)
    return(B)
a_list = [23,11,24]
counting(a_list,24)
