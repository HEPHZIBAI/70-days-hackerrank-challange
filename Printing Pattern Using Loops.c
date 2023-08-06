/*
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/printing-pattern-2/problem
*/





#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main() 
{

    int n;
    scanf("%d", &n);
    for(int i=1;i<2*n;i++)
    {
        for(int j=1;j<2*n;j++)
            if(abs(n-i)>abs(n-j))
                printf("%d ",abs(n-i)+1);
            else
                printf("%d ",abs(n-j)+1);
        
        printf("\n");
    }
}