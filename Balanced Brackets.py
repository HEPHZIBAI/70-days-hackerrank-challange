'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/balanced-brackets
'''





def isBalanced(s):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    for bracket in s:
        if bracket in opening_brackets:
            stack.append(bracket)
        else:
            if not stack:
                return "NO"  # Unmatched closing bracket
            last_opening_bracket = stack.pop()
            if opening_brackets.index(last_opening_bracket) != closing_brackets.index(bracket):
                return "NO"  # Unmatched opening and closing brackets

    if not stack:
        return "YES"  # All brackets were matched
    else:
        return "NO"  # Unmatched opening brackets

# Input
n = int(input().strip())
for _ in range(n):
    s = input().strip()
    print(isBalanced(s))
