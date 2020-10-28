class SelectionSort:
    def __init__(self,ar):
        self.arr=ar
    def sort(self,start=0):
        if start == len(self.arr)-1:
            return
        for i in range(start,len(self.arr)):
            if (self.arr[start]  >self.arr[i]):
                self.arr[start],self.arr[i]= self.arr[i],self.arr[start]
        self.sort(start+1)
    def sortIterative(self,reverse=False):
        if (reverse):
            for i in range(len(self.arr)):
                max = i
                for j in range(i+1,len(self.arr)):
                    if(self.arr[max] < self.arr[j]):
                        max =j
                self.arr[max],self.arr[i] = self.arr[i],self.arr[max]
        else:  
            for i in range(len(self.arr)):
                min = i
                for j in range(i+1,len(self.arr)):
                    if(self.arr[min] > self.arr[j]):
                        min =j
                self.arr[min],self.arr[i] = self.arr[i],self.arr[min]
                
    def print(self):
        print(self.arr)
arr= SelectionSort([23,54,2,43,10,8,18])
# arr.sort()
arr.sortIterative(True)
arr.print()
                
