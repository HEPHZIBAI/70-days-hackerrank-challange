'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/binary-search-tree-insertion
'''



def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert_helper(self.root, val)

    def _insert_helper(self, node, val):
        if val <= node.info:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert_helper(node.left, val)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert_helper(node.right, val)