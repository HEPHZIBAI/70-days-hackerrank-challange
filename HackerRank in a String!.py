'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/hackerrank-in-a-string
'''


def hackerrankInString(s):
    word = "hackerrank"
    index = 0

    for char in s:
        if char == word[index]:
            index += 1
            if index == len(word):
                return "YES"

    return "NO"

# Sample Input
queries = int(input())
# Sample Output
for i in range(queries):
    a=input()
    result = hackerrankInString(a)
    print(result)