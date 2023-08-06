/*
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/insert-a-node-at-a-specific-position-in-a-linked-list
*/




SinglyLinkedListNode* insertNodeAtPosition(SinglyLinkedListNode* llist, int data, int position) {
    SinglyLinkedListNode* newNode = create_singly_linked_list_node(data);

    if (position == 0) {
        // Insert at the head
        newNode->next = llist;
        return newNode;
    }

    SinglyLinkedListNode* current = llist;
    for (int i = 0; i < position - 1; i++) {
        current = current->next;
    }

    // Insert the new node after the current node at the desired position
    newNode->next = current->next;
    current->next = newNode;

    return llist;
}


