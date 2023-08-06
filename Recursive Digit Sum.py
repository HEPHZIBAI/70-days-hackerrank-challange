'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/recursive-digit-sum
'''





def super_digit(n, k):
    def recursive_super_digit(s):
        if len(s) == 1:
            return int(s)
        else:
            return recursive_super_digit(str(sum(int(digit) for digit in s)))

    concatenated_number = str(sum(int(digit) for digit in n) * k)
    return recursive_super_digit(concatenated_number)

a=input().split()
b=a[0]
c=int(a[1])
print(super_digit(b,c)) 