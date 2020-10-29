"""
kth Min Element present in the array
"""
def BubbleSort(ar,k):
    if k==1:
        return
    for i in range(k-1):
        if ar[i] > ar[i+1]:
            ar[i],ar[i+1] =ar[i+1],ar[i]
    return BubbleSort(ar,k-1)

def kthMin(ar,n):
    print(ar[n-1])
ar=[12,34,23,1,7,8]
BubbleSort(ar,len(ar))
print(ar)
kthMin(ar,3)
