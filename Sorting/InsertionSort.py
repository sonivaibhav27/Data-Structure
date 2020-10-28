class InsertionSort:
    def __init__(self,arr):
        self.arr=arr
    def sort(self):
        for i in range(1,len(self.arr)):
            value =self.arr[i]
            j=i-1
            #We will go backwards till value is not less than arr[j]
            #We will copy all values 
            while (j>=0 and self.arr[j] > value):
                self.arr[j+1] = self.arr[j]
                print(self.arr)
                j-=1
            self.arr[j+1] = value
    def print(self):
        print(self.arr)
ar = InsertionSort([12,3,23,2])
ar.sort()
ar.print()
