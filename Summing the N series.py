'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/summing-the-n-series
'''





def summingSeries(n):
    # The value of the nth term in the sequence is n^2 - (n-1)^2
    # Simplifying the above expression, we get n^2 - (n-1)^2 = 2n - 1
    # So, the sum of the series up to the nth term is 1 + 3 + 5 + ... + (2n - 1)
    # This is the sum of the odd numbers up to 2n - 1.
    # The sum of odd numbers up to n can be calculated using the formula (n * n)
    return (n * n) % (10**9 + 7)

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())
    result = summingSeries(n)
    print(result)
