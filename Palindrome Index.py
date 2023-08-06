'''https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/palindrome-index'''


def is_palindrome(s):
    return s == s[::-1]

def palindrome_index(s):
    if is_palindrome(s):
        return -1

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Try removing from the left side
            temp_left = s[:left] + s[left + 1:]
            if is_palindrome(temp_left):
                return left

            # Try removing from the right side
            temp_right = s[:right] + s[right + 1:]
            if is_palindrome(temp_right):
                return right

            # If both options result in non-palindromic strings, there is no solution
            return -1

        left += 1
        right -= 1

# Example usage:
a=int(input())
query_strings =[]
for i in range(a):
    query_strings.append(input())
#query_strings = ["aaab", "baa", "aaa"]
for s in query_strings:
    result = palindrome_index(s)
    print(result)
