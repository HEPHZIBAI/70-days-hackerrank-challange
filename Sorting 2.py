'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/sorting-2-1-1
'''




n=int(input())
a=list(map(int,input().split()))
x=int(input())
y=0
k=1
if(x>0):
    while(y<n):
        if(k%2!=0):
            h=a[y:y+x]
            y+=x
            h.sort()
            for i in h:
                print(i,end=" ")
        else:
            h=a[y:y+x]
            y+=x
            h.sort(reverse=True)
            for i in h:
                print(i,end=" ")
        k+=1
else:
    y=n
    p=[]
    while(y>=0):
        if(k%2!=0):
            h=a[y+x:y]
            y+=x
            h.sort(reverse=True)
            p+=h
        else:
            h=a[y+x:y]
            y+=x
            h.sort()
            p+=h
        k+=1
    p.reverse()
    for i in p:
        print(i,end=" ")