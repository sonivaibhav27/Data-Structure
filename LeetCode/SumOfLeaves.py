def sumOfLeafNodes(root):
    #Your code here
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data
    else:
        return sumOfLeafNodes(root.left)+sumOfLeafNodes(root.right)
