class Stack:
    def __init__(self,data):
        self.s = data
    def top(self):
        print(self.s[-1])
    def length(self):
        print(len(self.s))
    def print(self):
        print(self.s)
    def push(self,data):
        self.s.append(data)
        print(self.s)
    def pop(self):
        self.s.pop()
        print(self.s)
    def search(self,data):
        try:
            a = self.s.index(data)
            print(a)
        except ValueError:
            print("Element %s not found" %data)
s= Stack([1,2,3,4])
s.print()
s.push(20)
s.push(40)
s.pop()
s.search(23)
s.length()
