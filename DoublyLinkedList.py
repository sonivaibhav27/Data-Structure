class Node:
    def __init__(self,data):
        self.data = data
        self.prev=None
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    def addNode(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            temp = self.head
            while temp.next is not None:
                temp=temp.next
            a = Node(data)
            temp.next = a
            a.prev =temp
    def Print(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("NULL")
    def addAtBeg(self,data):
        a= Node(data)
        a.next =self.head
        self.head=a
    def removeAtBeginning(self):
        self.head =self.head.next
    def removeAtEnd(self):
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.prev.next =None
    def printEnd(self):
        temp=self.head
        while temp.next:
            temp=temp.next
        while temp.prev:
            print(temp.data,end="->")
            temp=temp.prev
        print(temp.data,end="->NULL")
        print()
    def insertAfter(self,insertAfter,data):
        a=Node(data)
        temp=self.head
        while temp.data != insertAfter:
            temp=temp.next
        a.next =temp.next
        temp.next=a
        
            
d = DLL()
d.addNode(10)
d.addNode(30)
d.addNode(20)
d.addNode(50)
d.addAtBeg(5)
d.removeAtBeginning()
d.removeAtEnd()
d.printEnd()
d.insertAfter(20,100)
d.Print()
d.printEnd()
