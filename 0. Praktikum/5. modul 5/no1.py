def towerofhanoi(n,start, dest, aux):
    if n == 1:
        print(" - Memindahkan lempengan %d dari %s ke %s"%(n,start,dest))
        if start == "A" and dest == "B":
            sortir(n,A,B)
        elif start == "A" and dest == "C":
            sortir(n,A,C)
        elif start == "B" and dest == "A":
            sortir(n,B,A)
        elif start == "B" and dest == "C":
            sortir(n,B,C)
        elif start == "C" and dest == "A":
            sortir(n,C,A)
        elif start == "C" and dest == "B":
            sortir(n,C,B)
        print("{} :\n{}\n{} :\n{}\n{} :\n{}".format(tower[0],display(A),tower[1],display(B),tower[2],display(C)))
    else:
        towerofhanoi(n-1,start,aux, dest)
        print("\n - Memindahkan lempengan %d dari %s ke %s"%(n,start,dest))
        if start == "A" and dest == "B":
            sortir(n,A,B)
        elif start == "A" and dest == "C":
            sortir(n,A,C)
        elif start == "B" and dest == "A":
            sortir(n,B,A)
        elif start == "B" and dest == "C":
            sortir(n,B,C)
        elif start == "C" and dest == "A":
            sortir(n,C,A)
        elif start == "C" and dest == "B":
            sortir(n,C,B)
        print("{} :\n{}\n{} :\n{}\n{} :\n{}".format(tower[0],display(A),tower[1],display(B),tower[2],display(C)))
        towerofhanoi(n-1, aux, dest, start)

def display(tower):
    temp = ""
    if len(tower) == 0 :
        return("")
    elif len(tower) == 1 :
        return("|{}|".format(tower[0]))
    else:
        for tower in tower:
            temp += "|{}|\n".format(tower)
        return(temp)

def sortir(n,start,dest):
    temp = start.pop(start.index(n))
    dest.insert(0,temp)


lst_num = [1,2,3,4]
tower = ["A","B","C"]
A = []
B = []
C = []
print("Memindahkan {} lempengan dari {} Menuju {} dengan bantuan {}".format(len(lst_num),tower[0],tower[2],tower[1]))
for num in lst_num:
    A.append(num)
print("{} :\n{}\n{} :\n{}\n{} :\n{}".format(tower[0],display(A),tower[1],display(B),tower[2],display(C)))
towerofhanoi(4,"A","C","B")
