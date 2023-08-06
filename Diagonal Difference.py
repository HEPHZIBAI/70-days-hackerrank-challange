'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/diagonal-difference
'''




def diagonalDifference(arr):
    # Get the size of the square matrix
    n = len(arr)

    # Initialize variables to store the sums of the diagonals
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0

    # Iterate through the elements and calculate the sums of diagonals
    for i in range(n):
        primary_diagonal_sum += arr[i][i]
        secondary_diagonal_sum += arr[i][n - 1 - i]

    # Calculate the absolute difference between the sums of diagonals
    absolute_difference = abs(primary_diagonal_sum - secondary_diagonal_sum)

    return absolute_difference

# Sample Input
n = int(input())
matrix = []
for i in range(n):
    a = list(map(int, input().split()))
    matrix.append(a)

# Calculate and print the result
result = diagonalDifference(matrix)
print(result)  # Output: 15
