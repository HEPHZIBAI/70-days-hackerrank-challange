'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/sherlock-and-divisors/copy-from/1365143647
'''




import math

def count_divisors_divisible_by_2(n):
    count = 0
    sqrt_n = int(math.sqrt(n))
    
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            if i % 2 == 0:
                count += 1
            if i != n // i and (n // i) % 2 == 0:
                count += 1
    
    return count

def main():
    t = int(input())
    for _ in range(t):
        num = int(input())
        result = count_divisors_divisible_by_2(num)
        print(result)

if __name__ == "__main__":
    main()
