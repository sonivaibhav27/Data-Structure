class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LL:
    def __init__(self):
        self.head = None
    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next is not None:
                temp=temp.next
            temp.next =  Node(data)
    def printLL(self):
        temp = self.head
        while temp:
            print(str(temp.data)+"->",end="")
            temp=temp.next
        print("Null")
    def length(self):
        count =1
        temp = self.head
        while temp.next is not None:
            count+=1
            temp = temp.next
        return count
    def insertAtBeginning(self,data):
        # previous head -> Dusre 
        temp = self.head
        beg = Node(data)
        beg.next = temp 
        self.head = beg
    # def detectLoop(self):
    #     slow = fast = self.head
        # while(slow and fast and fast.en)
    def removeAtBeginning(self):
        temp = self.head
        self.head = temp.next 
    def removeAtEnd(self):
        temp = self.head
        while temp.next is not None:
            temp =temp.next
        self.head = temp
    
            

l =  LL()
l.insert(20)
l.insert(30)
l.printLL()
l.insertAtBeginning(10)
l.printLL()
l.removeAtBeginning()
l.printLL()
print(l.length())
