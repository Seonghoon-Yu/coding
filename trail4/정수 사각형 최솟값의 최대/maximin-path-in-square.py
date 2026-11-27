n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# (1,1) 에서 오른쪽 혹은 밑칸, (N,N) 로 이동.
# 거쳐간 위치에 적혀져 있는 정수들 중 최솟값을 최대로


## DP 매열 정의
dp = [[0] * n for _ in range(n)]


## 초기값 정의
dp[0][0] = grid[0][0]
for i in range(1,n):
    dp[0][i] = min(dp[0][i-1], grid[0][i])
    dp[i][0] = min(dp[i-1][0], grid[i][0])



## 어떤 값을 ..?
## 경로의 최솟값의 최댓값?
## 경로의 최솟값을 dp에 저장


## dp에 최솟값을 저장해두고,
## dp[0][1] = min(dp[0][0], grid[0][1]) ->
## dp[1][1] = if grid[i][j] > max(dp[i-1][0], dp[0][j-1]): dp[1][1] = max ...
##              if grid[i][j] < ... dp[1][1] = grid[i][j]


for i in range(1, n):
    for j in range(1, n):
        
        dp[i][j] = max(min(dp[i][j-1], grid[i][j]), min(dp[i-1][j], grid[i][j]))

print(dp[n-1][n-1])