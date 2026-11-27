n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


## 정수 사각형 최장 증가 수열

## 시작점을 적절하게 잡아, 상하좌우 인접한 칸으로 계속 칸에 적혀있는 정수값이 커지도록 이동.
# 밝고 지나갈 수 있는 최대 칸의수 .


# 이전 state가 뭐였는지 생각하기.
# 현재값이 이전보다 크면 이전 값에서 + 1
# 만약에 주변이 자기보다 큰 값이 없으면 0
# 시작점에 따라 count가 달라질텐데. .. 이게 DP가 맞아?
# 이전 dp 값이 없으면 계산해서 구하고
# 이전 dp 값이 있으면 +1 ?


# dp 배결 정의
dp = [[1] * n for _ in range(n)]

block = [
    (0,1),
    (0,-1),
    (1,0),
    (-1,0)
]

# 초기값

# 점화식
'''
가장 작은 칸 부터 확인
dp[i][j] = 
for dr dy ..
'''
cells = []
for i in range(n):
    for j in range(n):
        cells.append((grid[i][j], i, j))

cells.sort(key=lambda x: (x[0],x[1],x[2]))


# 구현

for value, r, c in cells:
    
    for dr, dc in block:
        nr, nc = r+dr, c+dc
        if 0<=nr<n and 0<=nc<n:
            if grid[nr][nc] > grid[r][c]:
                dp[nr][nc] = max(dp[r][c] + 1, dp[nr][nc])


answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dp[i][j])

print(answer)