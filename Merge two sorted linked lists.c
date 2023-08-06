/*
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/merge-two-sorted-linked-lists
*/








// Complete the mergeLists function below.

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode* next;
 * };
 *
 */
SinglyLinkedListNode* mergeLists(SinglyLinkedListNode* head1, SinglyLinkedListNode* head2) {
 if (head1 == NULL) {
        return head2;
    }

    if (head2 == NULL) {
        return head1;
    }

    SinglyLinkedListNode* mergedHead;
    if (head1->data <= head2->data) {
        mergedHead = head1;
        head1 = head1->next;
    } else {
        mergedHead = head2;
        head2 = head2->next;
    }

    SinglyLinkedListNode* mergedCurrent = mergedHead;
    while (head1 != NULL && head2 != NULL) {
        if (head1->data <= head2->data) {
            mergedCurrent->next = head1;
            head1 = head1->next;
        } else {
            mergedCurrent->next = head2;
            head2 = head2->next;
        }
        mergedCurrent = mergedCurrent->next;
    }

    if (head1 != NULL) {
        mergedCurrent->next = head1;
    } else if (head2 != NULL) {
        mergedCurrent->next = head2;
    }

    return mergedHead;
}
