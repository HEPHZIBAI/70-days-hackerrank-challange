/*
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail
*/





int getNode(SinglyLinkedListNode* llist, int positionFromTail) {
    SinglyLinkedListNode* mainPtr = llist;
    SinglyLinkedListNode* refPtr = llist;

    // Move mainPtr to positionFromTail + 1 steps ahead
    for (int i = 0; i < positionFromTail + 1; i++) {
        if (!mainPtr) {
            // If positionFromTail is greater than the number of elements, return -1
            return -1;
        }
        mainPtr = mainPtr->next;
    }

    // Move mainPtr and refPtr simultaneously until mainPtr reaches the end
    while (mainPtr) {
        mainPtr = mainPtr->next;
        refPtr = refPtr->next;
    }

    // The refPtr is now at the desired position from the tail
    return refPtr->data;
}
