# Fungsi untuk membuat stack kosong 
# menginisialisasi size stack=0
def createStack(): 
	stack=[] 
	return stack 

# Fungsi untuk menentukan size atau ukuran stack
"""def size(stack): 
	return len(stack)""" 

# Stack bernilai kosong apabila ukurannya 0 
def isEmpty(stack): 
	if len(stack) == 0: 
		return true 

# Fungsi untuk menambah item pada stack 	 
def push(stack,item): 
	stack.append(item) 

# Fungsi untuk menghapus item pada stack 
def pop(stack): 
	if isEmpty(stack): return
	return stack.pop() 

#Fungsi untuk membalikkan string 
def reverse(string): 
	n = len(string) 
	
	# buat stack kosong
	stack = createStack() 

	# Push semua karakter string untuk ditumpuk
	for i in range(0,n,1): 
		push(stack,string[i]) 

	# Membuat string kosong 
	string="" 

	# Pop semua karakter string dan letakkan kembali ke dalam string 
	for i in range(0,n,1): 
		string+=pop(stack) 
		
	return string 

# Untuk mencetak hasil reverse kata menggunakan inputan dari user
s = input("Silakan masukkan kata : ")
print ("Kata awal : ",s) 
print ("Hasil reverse kata : ",reverse(s))
