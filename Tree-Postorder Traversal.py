'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/tree-postorder-traversal
'''




def postOrder(root):
    #Write your code here
    if root is not None:
        # Traverse left subtree
        postOrder(root.left)
        # Traverse right subtree
        postOrder(root.right)
        # Print the value of the current node
        print(root.info, end=' ')