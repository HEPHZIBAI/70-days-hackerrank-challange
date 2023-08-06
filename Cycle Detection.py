'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/detect-whether-a-linked-list-contains-a-cycle'''




def has_cycle(head):
    if not head:
        return 0

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return 0

        slow = slow.next
        fast = fast.next.next

    return 1