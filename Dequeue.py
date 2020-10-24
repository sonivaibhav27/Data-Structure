class Dequeue:
    def __init__(self,data):
        self.q = data
    def addFront(self,data,returnList=False):
        self.q.insert(0,data)
        if(returnList):
            return self.q
    def addBack(self,data):
        self.q.append(data)
    def removeFirst(self):
        self.q.pop(0)
    def removeLast(self):
        self.q.pop()
    def printQ(self,returnList=False):
        for i in self.q:
            print(i,sep="->")
        return self.q
    def firstElement(self):
        return self.q[0]
    def lastElement(self):
        return self.q[-1]
    def count(self):
        return len(self.q)
    def search(self,data):
        try:
            self.q.index(data)
            return True
        except ValueError:
            return False

q = Dequeue([1,4,54,23,90,80,34,23])
q.addFront(10)
# q.printQ()
q.removeFirst()
# q.printQ()
q.removeLast()
# q.printQ()
print(q.firstElement())
print(q.search(5))
