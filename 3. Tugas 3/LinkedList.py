class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head==None
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def display(self):
        current=self.head
        while current != None:
            print(current.getData())
            current = current.getNext()
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count+=1
            current = current.getNext()
        return count
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current=current.getNext()
        return found
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    
    def insertPrevious(self,item,previous_item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == previous_item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            temp = Node(item)
            temp.setNext(self.head)
            self.head = temp
        else:
            temp = Node(item)
            temp.setNext(current)
            previous.setNext(temp)
    
    def insertNext(self,item,previous_item):
        current = self.head
        next_item = current.getNext()
        found = False
        while not found:
            if current.getData() == previous_item:
                found = True
            else:
                current = next_item
                next_item = current.getNext()
        if next_item == None:
            temp = Node(item)
            current.setNext(temp)
        else:
            temp = Node(item)
            temp.setNext(next_item)
            current.setNext(temp)

listku = LinkedList()

listku.add(10)
listku.add(20)
listku.add(30)
listku.insertPrevious(5,30)
listku.insertNext(9,20)
listku.display()

