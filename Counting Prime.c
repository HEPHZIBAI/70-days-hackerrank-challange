/*
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/counting-primes-2-1
*/



#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main() 
{
    int n;
    scanf("%d",&n);
    int p=0,c=0,m;
    for(int i=1;i<n;i++)
    {
        m=1;
        for(int j=2;j<i;j++)
        {
            if(i%j==0)
            {
                m=0;
                break;
            }
        }
        if(i==1)
            c++;
        if(m==1)
            p++;
        else
            c++;
    }
   // printf("%d %d",c,(p/2)+1);
    printf("%d",c+1+(p/2));
    return 0;
}