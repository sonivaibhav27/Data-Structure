# Linear Search
def BinarySearch(arr,key,l,r):
    print(l,r)
    if(r >=l):
        mid = (l+r)//2
        if(arr[mid] == key):
            return mid
        elif(arr[mid] < key):
            return BinarySearch(arr,key,mid+1,r)
        else:
            return BinarySearch(arr,key,l,mid-1)
    else:
        return -1
    
n = int(input("Enter the Number of Element to Search From: "))

arr = list(map(int,input().split()))
k = int(input("Enter the Number to be Search: "))
print(BinarySearch(arr,k,0,n-1))
