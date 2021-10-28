import stack as st

def cek(infix):
    data = st.stack()
    kurung = {')':'(',']':'[','}':'{',}
    for i in infix:
        if i in kurung.values():
            st.push(data,i)
        elif i in kurung.keys():
            if st.isEmpty(data):
                print ('Jumlah kurung tutup terlalu banyak')
                return False
            elif st.peek(data) != kurung[i]:
                print ('kurung buka dan kurung tutup tidaklah cocok')
                return False
            else:
                st.pop(data)
    if st.isEmpty(data):
        return True
    else:
        print ('Jumlah kurung buka terlalu banyak')
        return False

def in2post(infix):
    cekkurung = '()[]{}'
    cekoperator = '+-*/'
    cekspasi = ''
    angka = '1234567890'
    for i in infix:
        if i in angka:
            if cekspasi == '' or cekspasi[-1] in angka :
                cekspasi += i
            else:
                cekspasi += ' '
                cekspasi += i
        elif i in cekkurung:
            cekspasi += ' '
            cekspasi += i
        else:
            cekspasi += ' '
            cekspasi += i
            
    operator = {'+':1,'-':1,'*':2,'/':2,'(':0,'[':0,'{':0}
    kurung = {')':'(',']':'[','}':'{'}
    data = st.stack()
    inf = cekspasi.split()
    postfix = []
    for i in inf:
        if i.isdigit():
            postfix.append(i)
        elif i in kurung.keys():
            while not (st.peek(data) is kurung[i]):
                postfix.append(st.pop(data))
            st.pop(data)
        elif i in kurung.values():
            st.push(data,i)
        else:
            if not st.isEmpty(data):
                if operator[st.peek(data)] >= operator[i]:
                    postfix.append(st.pop(data))
                    st.push(data,i)
                else:
                    st.push(data,i)
            else:
                st.push(data,i)
    while not st.isEmpty(data):
            postfix.append(st.pop(data))
    return ' '.join(postfix)

def hitung(postfix):
    data = st.stack()
    post = postfix.split()
    for i in post:
        if i.isdigit():
            st.push(data,int(i))
        else:
            ope2 = st.pop(data)
            ope1 = st.pop(data)
            hasil = operasi(i,ope1,ope2)
            st.push(data,hasil)
    return st.pop(data)

def operasi(op,ope1,ope2):
    if op == '+':
        return ope1 + ope2
    elif op == '-':
        return ope1 - ope2
    elif op == '*':
        return ope1 * ope2
    else:
        return ope1 / ope2
    

n = input('Masukkan string operasi aritmatika = ')
if cek(n):
    postfix = in2post(n)
    print("infix :",n,"; postfix :",in2post(n),"=",hitung(in2post(n)))

