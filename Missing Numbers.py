'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/missing-numbers
'''



a=int(input())
x=list(map(int,input().split()))
q=set(x)
b=int(input())
y=list(map(int,input().split()))
w=set(y)
l=set()
for i in q:
    if(x.count(i)==y.count(i)):
        continue
    else:
        l.add(i)
        #print(i,end=" ")
for i in w:
    if(x.count(i)==y.count(i)):
        continue
    else:
        l.add(i)
        #print(i,end=" ")
l=list(l)
l.sort()
for i in l:
    print(i,end=" ")