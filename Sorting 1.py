'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/basic-sorting-1
'''




g=int(input())
h=list(map(int,input().split()))
p=[]
n=[]
for i in h:
    if i>=0:
        p.append(i)
    else:
        n.append(i)
p.sort()
n.sort(reverse=True)
x=y=0
for i in h:
    if i>=0:
        print(p[x],end=" ")
        x+=1
    else:
        print(n[y],end=" ")
        y+=1