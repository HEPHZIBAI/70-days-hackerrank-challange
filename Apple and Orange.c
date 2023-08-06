/*
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/apple-and-orange
*/

#include<stdio.h>
int main()
{
    int s,t;
    scanf("%d %d",&s,&t);
    int a,b;
    scanf("%d %d",&a,&b);
    int m,n;
    scanf("%d %d",&m,&n);
    int x[m],y[n];
    int u=0,q=0;
    for(int i=0;i<m;i++)
    {
        scanf("%d",&x[i]);
        x[i]+=a;
        if(x[i]>=s&&x[i]<=t)
            u++;
    }
    for(int i=0;i<n;i++)
    {
        scanf("%d",&y[i]);
        y[i]+=b;
        if(y[i]<=t&&y[i]>=s)
            q++;
    }
    printf("%d\n%d",u,q);
}