'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/anagram
'''



def count_characters_to_change(s):
    # Check if the length of the string is even
    if len(s) % 2 != 0:
        return -1

    # Split the string into two equal-length substrings
    half_length = len(s) // 2
    substring1 = s[:half_length]
    substring2 = s[half_length:]

    # Count the occurrences of each character in both substrings
    char_count_sub1 = [0] * 26
    char_count_sub2 = [0] * 26

    for char in substring1:
        char_count_sub1[ord(char) - ord('a')] += 1

    for char in substring2:
        char_count_sub2[ord(char) - ord('a')] += 1

    # Determine the characters to be changed to form an anagram
    characters_to_change = 0
    for i in range(26):
        characters_to_change += abs(char_count_sub1[i] - char_count_sub2[i])

    return characters_to_change // 2

def anagram(s):
    return count_characters_to_change(s)


a=int(input())
for i in range(a):
    test_case=input()
    result = anagram(test_case)
    print(result)