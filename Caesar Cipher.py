'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/caesar-cipher-1
'''




def caesarCipher(s, k):
    encrypted_string = ""

    for ch in s:
        if ch.isalpha():  # Check if the character is a letter
            base = 'A' if ch.isupper() else 'a'
            encrypted_char = chr((ord(ch) - ord(base) + k) % 26 + ord(base))
        else:
            encrypted_char = ch  # Non-letter characters remain unchanged
        encrypted_string += encrypted_char

    return encrypted_string

# Test the function with the provided sample input
a=int(input())
unencrypted_string = input()
rotation_factor = int(input())
result = caesarCipher(unencrypted_string, rotation_factor)
print(result)  # Output: "okffng-Qwvb"
