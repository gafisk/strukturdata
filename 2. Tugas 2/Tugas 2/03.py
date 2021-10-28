class Stack:
     def __init__(self):
          self.items = []

     def isEmpty(self):
          return self.items == []

     def push(self, item):
          self.items.append(item)

     def pop(self):
          return self.items.pop()

     def peek(self):
          return self.items[-1]

def convert(value):
     prec = {}
     prec["*"] = 3
     prec["/"] = 3
     prec["+"] = 2
     prec["-"] = 2
     prec["("] = 1

     obj = Stack()
     postfixList = []
     tokenList = value.split()
     print(tokenList,'\n')

     for token in tokenList:
          if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
               postfixList.append(token)
          elif token == ')':
               obj.push(token)
          elif token == '(':
               topToken = obj.pop()

               while topToken != ')':
                    postfixList.append(topToken)
                    topToken = obj.pop()

          else:
               while(not obj.isEmpty()) and \
                         (prec[obj.peek()] >= prec[token]):
                    postfixList.append(obj.pop())
               obj.push(token)
          print('isi Postfix ',str(postfixList))

     while not obj.isEmpty():
          postfixList.append(obj.pop())
     print('isi Postfix ',str(postfixList))
     print('\nHasil conversi : ',end='')
     return ' '.join(postfixList)

print(convert('A * B - C * D'))
