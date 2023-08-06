/*
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/kth-largest-and-smallest-element-in-an-array
*/



#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n, i, j, temp, c = 0;
    scanf("%d", &n);
    int arr[n];
    
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    
    int k;
    scanf("%d", &k);
    
    for (i = 0; i < n; i++) {
        for (j = i; j < n; j++) {
            if (arr[i] > arr[j]) {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
     int isDuplicate = 0;
        for (i = 0; i < n - 1; i++) {
            if (arr[i] == arr[i + 1]) {
                isDuplicate = 1;
                break;
            }
        }
    if (n == 0) {
        printf("-1\n");
    } else if (k > n || k < 0) {
        printf("%d %d\n", arr[0], arr[n - 1]);
    } else  if (isDuplicate) {
            printf("-1 -1\n");
    } else {
        printf("%d %d\n", arr[k - 1], arr[n - k]);
    }
    
    return 0;
}