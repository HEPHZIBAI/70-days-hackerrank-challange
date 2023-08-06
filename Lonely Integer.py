'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/lonely-integer
'''





def lonelyinteger(a):
    # Initialize a variable to store the XOR result
    unique_element = 0
    
    # Perform XOR on all elements in the array
    for num in a:
        unique_element ^= num
    
    return unique_element
a=int(input())
b=list(map(int,input().split()))
print(lonelyinteger(b))       