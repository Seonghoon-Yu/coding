import sys
sys.setrecursionlimit(10_000)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

###### k 1~100 까지 완전 탐색
###### 각 K 마다 안전영역 수 확인
###### K 이하인 집은 visited
###### 남아있는 집들 dfs로 다 visited로 만들고 dfs가 끝나면 count += 1

block = [
    (0,1),
    (0,-1),
    (1,0),
    (-1,0)

]
def dfs(r,c):


    visited[r][c] = True

    if grid[r][c] <= k:
        return

    for dx, dy in block:
        if 0 <= r+dx < n and 0 <= c+dy < m:
            if not visited[r+dx][c+dy]:
                dfs(r+dx, c+dy)
    

max_count = 0
min_k =1




for k in range(1,101):
    visited = [[False] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] <= k:
                visited[i][j]=True
    count = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                dfs(i,j)
                count += 1
    
    if max_count < count:
        max_count = count
        min_k = k

print(min_k, max_count)