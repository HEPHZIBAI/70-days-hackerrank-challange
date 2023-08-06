'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/spiral-matrix-58
'''




def print_spiral_pattern(size):
    if size == 0:
        print(-1)
        return

    # Initialize the matrix with zeros
    spiral_matrix = [[0 for _ in range(size)] for _ in range(size)]

    # Initialize variables for the boundaries and the current number
    top = 0
    bottom = size - 1
    left = 0
    right = size - 1
    num = 1

    while num <= size * size:
        # Move from left to right
        for i in range(left, right + 1):
            spiral_matrix[top][i] = num
            num += 1
        top += 1

        # Move from top to bottom
        for i in range(top, bottom + 1):
            spiral_matrix[i][right] = num
            num += 1
        right -= 1

        # Move from right to left
        for i in range(right, left - 1, -1):
            spiral_matrix[bottom][i] = num
            num += 1
        bottom -= 1

        # Move from bottom to top
        for i in range(bottom, top - 1, -1):
            spiral_matrix[i][left] = num
            num += 1
        left += 1

    # Find the maximum width of any number in the spiral matrix
    max_width = len(str(size * size))

    # Print the spiral pattern
    for row in spiral_matrix:
        for num in row:
            # Print each number with the appropriate spacing
            #print(f"{num:{max_width}}", end="\t")
            print(num,end="\t")
        print()

# Test the function
size = int(input())
print_spiral_pattern(size)