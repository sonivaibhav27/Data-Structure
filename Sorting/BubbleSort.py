def BubbleSort(arr):
    #Outer Loop will run for len(arr) -1
    #Inner Loop will run for 
    """
    1st Time it will run for 0 to 4
    2nd => 0 to 3 as we know that largest element has been at the end
    3nd=>0 to 2
    4th => 0 to 1
    """
    for i in range(len(arr) -1):
        for j in range(len(arr) - i -1):
            #Checking for the adjacent Elements
            if(arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    # print(arr)
    print(arr)
    
    
BubbleSort([10,30,2,4,24,18])
