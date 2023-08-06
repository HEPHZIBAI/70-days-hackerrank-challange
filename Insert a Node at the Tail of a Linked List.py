'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/insert-a-node-at-the-tail-of-a-linked-list
'''




def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)
    
    if head is None:
        # If the list is empty, the new node becomes the head
        head = new_node
    else:
        current = head
        while current.next is not None:
            current = current.next
        current.next = new_node
    
    return head
