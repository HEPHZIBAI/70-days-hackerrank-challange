'''
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/climbing-the-leaderboard/problem
'''




def climbingLeaderboard(ranked, player):
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                right = mid - 1
            else:
                left = mid + 1

        return left

    ranked = sorted(set(ranked), reverse=True)
    player_ranks = []

    for score in player:
        index = binary_search(ranked, score)
        player_ranks.append(index + 1)

    return player_ranks

# Example usage:
a=input()
leaderboard_scores = list(map(int,input().split()))
b=int(input())
player_scores = list(map(int,input().split()))
result = climbingLeaderboard(leaderboard_scores, player_scores)
for i in result:
    print(i) 
