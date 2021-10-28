#Desimal to biner
class Stack:
    def _init_(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def desimalkebiner(desimal):
    s=Stack()
    while desimal > 0:
        sisa= desimal % 2
        desimal= desimal //2
        s.push(sisa)
    biner=''
    while not s.is_empty():
        biner=biner+str(s.pop())
    return biner
print(desimalkebiner(8))
