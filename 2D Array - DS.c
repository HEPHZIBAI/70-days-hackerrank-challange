/*https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/2d-array*/




#include <stdio.h>
#include <limits.h>

int hourglassSum(int arr[6][6]) {
    int maxSum = INT_MIN; // Initialize maxSum to the smallest possible integer

    // Iterate through each hourglass
    for (int i = 0; i <= 3; i++) {
        for (int j = 0; j <= 3; j++) {
            // Calculate the sum of the current hourglass
            int sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] +
                      arr[i + 1][j + 1] +
                      arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2];

            // Update maxSum if the current sum is greater
            if (sum > maxSum) {
                maxSum = sum;
            }
        }
    }

    return maxSum;
}

int main() {
    int arr[6][6];

    // Read the input array
    for (int i = 0; i < 6; i++) {
        for (int j = 0; j < 6; j++) {
            scanf("%d", &arr[i][j]);
        }
    }

    int result = hourglassSum(arr);
    printf("%d\n", result);

    return 0;
}
