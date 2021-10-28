def createStack():
     stack = []
     return stack

def isEmpty(stack):
     if len(stack)==0:
          return True

def push(stack, item):
     stack.append(item)

def pop(stack):
     if isEmpty(stack): return
     return stack.pop()

def reverse(string):
     n = len(string)

     stack = createStack()

     for huruf in range(0, n, 1):
          push(stack,string[huruf])

     string=''

     for huruf in range(0, n, 1):
          string += pop(stack)

     return string

kata = input('Masukkan kata : ')
print('\nKata sebelum di reverse [%s]' % kata)
print('\nKata setelah di reverse [%s]' % reverse(kata))
