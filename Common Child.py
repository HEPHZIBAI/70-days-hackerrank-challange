'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/common-child
'''




def commonChild(s1, s2):
    n = len(s1)
    m = len(s2)
    
    # Initialize a 2D array with zeros to store the lengths of common children
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill the dp array
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The bottom-right cell of dp array contains the length of the longest common child
    return dp[n][m]

a=input()
b=input()
print(commonChild(a,b)) 
