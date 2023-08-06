/*
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/sorting-3-1-1
*/




#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    scanf("%d", &n);
    
    long int *a = (long int*)malloc(n * sizeof(long int));
    
    if (a == NULL) {
        printf("Memory allocation failed. Exiting...\n");
        return 1;
    }

    for (int i = 0; i < n; i++)
        scanf("%ld", &a[i]);

    int start = 0, max_length = 1, current_length = 1;
    int longest_start = 0, longest_end = 0;

    for (int i = 1; i < n; i++) {
        if (a[i] >= a[i - 1]) {
            current_length++;
        } else {
            if (current_length > max_length) {
                max_length = current_length;
                longest_start = start;
                longest_end = i - 1;
            }
            current_length = 1;
            start = i;
        }
    }

    if (current_length > max_length) {
        max_length = current_length;
        longest_start = start;
        longest_end = n - 1;
    }

    for (int i = longest_start; i <= longest_end; i++) {
        printf("%ld ", a[i]);
    }

    free(a);
    return 0;
}
