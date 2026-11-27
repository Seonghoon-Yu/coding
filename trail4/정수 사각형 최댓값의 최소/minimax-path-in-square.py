n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


## 정수 사각형 최댓값의 최소

# 가능한 경로 중 최댓값을 최소로..

# min(dp, dp), max(dp,grid)
# 오른쪽 혹은 밑

# dp 배열
dp = [[0] * n for _ in range(n)]

# 초기값
dp[0][0] = grid[0][0]

for i in range(1, n):
    dp[0][i] = max(dp[0][i-1], grid[0][i])
    dp[i][0] = max(dp[i-1][0], grid[i][0])


## 구현
for i in range(1, n):
    for j in range(1, n):
        prev = min(dp[i-1][j], dp[i][j-1])
        dp[i][j] = max(prev,grid[i][j])

print(dp[n-1][n-1])