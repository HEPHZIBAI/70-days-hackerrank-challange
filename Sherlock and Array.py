'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/sherlock-and-array
'''





def balancedSums(arr):
    total_sum = sum(arr)
    left_sum = 0
    
    for num in arr:
        if left_sum == total_sum - left_sum - num:
            return "YES"
        left_sum += num
    
    return "NO"

# Test cases
if __name__ == "__main__":
    t = int(input())  # Number of test cases
    for _ in range(t):
        n = int(input())  # Number of elements in the array
        arr = list(map(int, input().split()))  # Array of integers
        result = balancedSums(arr)
        print(result)
