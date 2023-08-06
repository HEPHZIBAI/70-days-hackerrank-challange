/*
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/icecream-parlor
*/



#include<stdio.h>
int main() {
    int t;
    scanf("%d", &t);
    
    while (t!=0) {
        int money, n;
        scanf("%d", &money);
        scanf("%d", &n);
        
        int flavors[n];
        for (int i = 0; i < n; i++) {
            scanf("%d", &flavors[i]);
        }
        
        t--;
        for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (flavors[i] + flavors[j] == money) {
                printf("%d %d\n", i + 1, j + 1);
            }
        }
    }
    }
    
    return 0;
}