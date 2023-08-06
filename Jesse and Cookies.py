'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/jesse-and-cookies
'''





import heapq

def cookies(k, A):
    # Convert the list A to a min heap
    heapq.heapify(A)
    operations = 0
    
    while A[0] < k:
        # If there's only one cookie left and its sweetness is still less than k, it's not possible to reach the threshold.
        if len(A) == 1:
            return -1
        
        # Get the two least sweet cookies and combine them
        least_sweet_cookie = heapq.heappop(A)
        second_least_sweet_cookie = heapq.heappop(A)
        combined_sweetness = least_sweet_cookie + 2 * second_least_sweet_cookie
        
        # Add the combined cookie back to the heap
        heapq.heappush(A, combined_sweetness)
        operations += 1
    
    return operations

# Test example
l=list(map(int,input().split()))
size, threshold =l[0],l[1]
cookies_list = list(map(int,input().split()))
print(cookies(threshold, cookies_list))  # Output: 2
