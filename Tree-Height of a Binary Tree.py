'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/tree-height-of-a-binary-tree
'''





if root is None:
        return -1  # Height of an empty tree is -1

    left_height = height(root.left)
    right_height = height(root.right)

    # Return the maximum height between the left and right subtrees plus 1 for the current node
    return max(left_height, right_height) + 1