'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/pangrams
'''





def pangrams(s):
    # Convert the sentence to lowercase
    s = s.lower()

    # Create a set to store unique letters
    unique_letters = set()

    # Iterate through each character in the sentence
    for char in s:
        # Ignore non-alphabetic characters
        if char.isalpha():
            unique_letters.add(char)

    # Check if the set contains all 26 letters of the English alphabet
    if len(unique_letters) == 26:
        return "pangram"
    else:
        return "not pangram"

# Test cases
s=input()
print(pangrams(s))