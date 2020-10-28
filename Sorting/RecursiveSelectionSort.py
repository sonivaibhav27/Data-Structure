class SelectionSort:
    def __init__(self,ar):
        self.arr=ar
    def sort(self,start=0):
        if start == len(self.arr)-1:
            return
        for i in range(start,len(self.arr)):
            if (self.arr[start]  >self.arr[i]):
                self.arr[start],self.arr[i]= self.arr[i],self.arr[start]
            print(str(i)+"->" + str(self.arr))
        self.sort(start+1)
    def print(self):
        print(self.arr)
arr= SelectionSort([23,54,2,43,10,8,18])
arr.sort()
arr.print()
                
