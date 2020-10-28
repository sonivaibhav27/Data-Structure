def QuickSort(a,start,end):
    #Partioning will return the pivot index
    #We select pivot because all the elements lesser than pivot become
    #left to the pivot and all the elements greater than pivot are to the
    #right of pivot
    print(a)
    if start >= end:
        return
    pivotIndex = Partition(a,start,end)
    QuickSort(a,start,pivotIndex-1)
    QuickSort(a,pivotIndex+1,end)
def Partition(a,start,end):
    pivot = a[end]
    partitionIndex= start
    for i in range(start,end):
        if(a[i] <= pivot):
            a[partitionIndex],a[i]=a[i],a[partitionIndex]
            partitionIndex+=1
    a[partitionIndex],a[end] = a[end],a[partitionIndex]
    return partitionIndex

a=[2,1,34,2,32,25,17]
QuickSort(a,0,6)
print(a)
        
