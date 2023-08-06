'''https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/largest-permutation'''




def largestPermutation(k, arr):
    n = len(arr)
    num_to_index = {num: i for i, num in enumerate(arr)}
    
    for i in range(n):
        if k == 0:
            break

        if arr[i] != n - i:
            # Swap the current number with the largest possible number
            max_num = n - i
            max_num_index = num_to_index[max_num]
            arr[i], arr[max_num_index] = arr[max_num_index], arr[i]
            
            # Update the mapping of numbers to their indices
            num_to_index[arr[i]], num_to_index[arr[max_num_index]] = i, max_num_index
            
            k -= 1

    return arr

# Input reading from STDIN
n, k = map(int, input().split())
arr = list(map(int, input().split()))

result = largestPermutation(k, arr)
print(*result)
