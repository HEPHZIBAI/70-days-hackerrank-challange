/*
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/pattern-1-38-1
*/




#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        printf("%d ",i);
        for(int j=1;j<i-1;j++)
            printf("0 ");
        if(i>1)
            printf("%d ",i);
        printf("\n");
    }
    for(int i=n-1;i>=1;i--)
    {
        printf("%d ",i);
        for(int j=1;j<i-1;j++)
            printf("0 ");
        if(i>1)
            printf("%d ",i);
        printf("\n");
    }
    return 0;
}
