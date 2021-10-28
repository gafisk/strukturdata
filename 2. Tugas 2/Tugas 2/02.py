class Stack:
     def __init__ (self):
          self.items = []

     def isEmpty(self):
          return self.items==[]

     def push(self, num):
          self.items.append(num)

     def pop(self):
          return self.items.pop()

     def peek(self):
          return self.items[-1]

decimal=0
binary=''

decimal=int(input('Masukkan nilai Desimal : '))
print('Nilai dalam Desimal\t: %d' % decimal)

obj = Stack()

while decimal>0:
     obj.push(decimal%2)
     decimal=decimal//2
     
while obj.isEmpty()==False:
     binary=binary+str(obj.pop())

print('Nilai dalam Biner\t: %s ' % binary)
