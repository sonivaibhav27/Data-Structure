class PriorityQ:
    p =[] 
    e=[]
    def __init__(self):
        pass
    def insert(self,data,priority):
        self.e.append(data)
        self.p.append(priority)
    def removeElement(self):
        a = max(self.p)
        a = self.p.index(a)
        self.e.pop(a)
        self.p.pop(a)
        return True
    def print(self):
        for i in range(len(self.p)):
            print(str(self.p[i])+ "->"+ str(self.e[i]))
            
            
        

pq = PriorityQ()
pq.insert(20,4)
pq.insert(30,3)
pq.insert(40,7)
pq.insert(50,1)
pq.insert(60,2)
# pq.print()
pq.removeElement()
pq.print()
