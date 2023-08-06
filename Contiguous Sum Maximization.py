'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/contiguous-sum-maximization
'''






n=int(input())
a=list(map(int,input().split()))
l=-1000000000
if(n==1):
    print(a[0])
else:
    for i in range (len(a)):
        for j in range(i+1,len(a)+1):
            b=a[i:j]
            s=0
            for k in b:
                s+=k
            if(s>l):
                l=s
            #print(i,j,end=" ")
        #print("\n")
    print(l)
            