n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

'''
NxN 행렬, (1, 1) 에서 시작해서 오른쪽 혹은 밑으로만 이동하여 (N, N) 으로 감.
거쳐간 위치에 적혀져 있는 정수의 합
'''

## DP 배열 정리
dp = [[0] * n for _ in range(n)]


## DP 초기값
# dp[0][0] = grid[0][0]
dp[0][0] = grid[0][0]
for i in range(1, n):
    dp[0][i] = grid[0][i] + dp[0][i-1]
    dp[i][0] = grid[i][0] + dp[i-1][0]
#     dp[i][0] = grid[i][0]


## 점화식
## 이전 state가 2개.
# 둘중 하나 max
# print(dp)

## 구현

for i in range(n):
    for j in range(n):
        if i >= 1 and j >= 1:
            dp[i][j] = max(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])



# print(dp)
print(dp[n-1][n-1])