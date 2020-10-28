class RecursiveBubbleSort:
    def __init__(self,arr):
        self.arr =arr
    #N = Len of array
    def BubbleSort(self,n):
        if n ==1:
            return 
        for i in range(n-1):
            if(self.arr[i] > self.arr[i+1]):
                self.arr[i],self.arr[i+1]=self.arr[i+1],self.arr[i]
        self.BubbleSort(n-1)
    def print(self):
        print(self.arr)
bs = RecursiveBubbleSort([20,3,12,56,15,2,9])

bs.BubbleSort(7)

bs.print()
