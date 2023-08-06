'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/print-the-elements-of-a-linked-list
'''





def printLinkedList(head):
    current = head
    while current:
        print(current.data)
        current = current.next




