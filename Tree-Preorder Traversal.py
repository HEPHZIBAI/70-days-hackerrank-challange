'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/tree-preorder-traversal
'''




if root is not None:
        print(root.info, end=" ")
        preOrder(root.left)
        preOrder(root.right)