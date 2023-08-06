'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/searching-1-2-1
'''



n=int(input())
a=list(map(int,input().split()))
h=int(input())
if(h in a):
    print(a.index(h)+1)
else:
    print("-1")