# Linear Search
def LinearSearch(arr,key):
    for i in arr:
        if i == key:
            return "Element Found at index %s"%arr.index(i)
    return -1
    
n = int(input("Enter the Number of Element to Search From: "))

arr = list(map(int,input().split()))
k = int(input("Enter the Number to be Search: "))

print(LinearSearch(arr,k))
