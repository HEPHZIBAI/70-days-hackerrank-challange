'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/tree-inorder-traversal
'''



if root:
        inOrder(root.left)
        print(root.info, end=' ')
        inOrder(root.right)