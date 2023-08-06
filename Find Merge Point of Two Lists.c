/*
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/find-the-merge-point-of-two-joined-linked-lists/problem
*/








// Complete the findMergeNode function below.

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode* next;
 * };
 *
 */
int findMergeNode(SinglyLinkedListNode* head1, SinglyLinkedListNode* head2) {
    // Helper function to calculate the length of a linked list
    int getLinkedListLength(SinglyLinkedListNode* head) {
        int length = 0;
        while (head != NULL) {
            length++;
            head = head->next;
        }
        return length;
    }

    // Get the lengths of both linked lists
    int length1 = getLinkedListLength(head1);
    int length2 = getLinkedListLength(head2);

    // Find the difference in lengths
    int diff = abs(length1 - length2);

    // Move the pointer of the longer list forward by the difference
    if (length1 > length2) {
        while (diff > 0) {
            head1 = head1->next;
            diff--;
        }
    } else {
        while (diff > 0) {
            head2 = head2->next;
            diff--;
        }
    }

    // Traverse both lists until they meet at the merge point
    while (head1 != head2) {
        head1 = head1->next;
        head2 = head2->next;
    }

    // Return the data value at the merge point
    return head1->data;

}