#Two Technique 
arr =[1,4,5,7,12,20,35,50]
k=19
def pointer():
    j = len(arr)-1
    i=0
    while (i<j):
        if arr[i] + arr[j] == k:
            return [arr[i],arr[j]]
        elif arr[i] + arr[j] < k:
            i+=1
        else:
            j-=1

print(pointer())
