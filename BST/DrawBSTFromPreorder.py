class Node:
    def __init__(self,data):
        self.data= data
        self.left =None
        self.right=None
class BST:
    def __init__(self):
        self.root =None
    def insertElement(self,dataOfArr):
        self.root= Node(dataOfArr[0])
        
        i  = 1
        while i < len(dataOfArr):
            if dataOfArr[i] < self.root.data:
                if self.root.left is None:
                    self.root.left =Node(dataOfArr[i])
                else:
                    temp =self.root
                    while temp.left:
                        temp=temp.left
                    if temp.data >  dataOfArr[i]:
                        temp.left = Node(dataOfArr[i])
                    else:
                        temp.right = Node(dataOfArr[i])
            else:
                if self.root.right is None:
                    self.root.right = Node(dataOfArr[i])
                else:
                    temp =self.root
                    while temp.right:
                        temp=temp.right
                    temp.right = Node(dataOfArr[i])  
            i+=1
    def printTree(self):
        print(self.root.left.left.right.data)
        
        
# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.data)
#         inorder(root.right)
    
b=BST()
b.insertElement([8,5,1,7,10,12])
b.printTree()
