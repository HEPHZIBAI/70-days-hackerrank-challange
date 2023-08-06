'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/binary-to-gray
'''



def binary_to_gray(n):
    return n ^ (n >> 1)

# Input from the user (decimal representation of the binary number)
n = int(input())

# Convert the decimal to its corresponding Gray code
gray_code = binary_to_gray(n)

# Output the result
print(gray_code)
