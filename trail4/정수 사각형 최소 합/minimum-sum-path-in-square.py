n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

## (1,N)에서 시작 왼쪽 혹은 밑으로만 이동하여 (N,1) 로 감.


## dp 배열 정의
dp = [[0] * n for _ in range(n)]

dp[0][n-1] = grid[0][n-1]

## 초기값
for i in range(1, n):
    dp[i][n-1] = dp[i-1][n-1] + grid[i][n-1]

for i in range(n-2, -1, -1):
    dp[0][i] = dp[0][i+1] + grid[0][i]


## 점화식

## dp[i][j] = max(dp[i-1][j]+grid[i][j], dp[i][j+1] + grid[i][j])


for i in range(n):
    for j in range(n-1, -1, -1):
        # print(i,j)
        if dp[i][j] == 0:
            dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j+1] + grid[i][j])
# print(dp)
print(dp[n-1][0])

