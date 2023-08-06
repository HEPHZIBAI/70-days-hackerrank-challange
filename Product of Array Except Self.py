'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/product-of-array-except-self-5
'''




a=list(map(int,input().split()))
if(a.count(0)>1):
    print('0 '*len(a))
else:
    p=1
    for i in range(len(a)):
        p=1
        for j in range(len(a)):
            if(i!=j):
                p*=a[j]
        print(p,end=" ")