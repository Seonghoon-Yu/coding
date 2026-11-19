from copy import copy
import sys
sys.setrecursionlimit(10**6)

n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

r = []
c = []
for _ in range(k):
    ri, ci = map(int, input().split())
    r.append(ri - 1)
    c.append(ci - 1)

# Please write your code here.

### M개의 돌만 적절하게 치워, K개의 시작점으로 상하좌우 인접한 곳으로만 이동하여 도달 가능한 칸의 수를 최대.

# BFS로 최대 가능한 칸수 계산
# 모든 가능한 돌을 치워서 최대 가능한 칸수?
# 꼭 M개의 돌을 치워야함.

## 돌을 치운 모든 경우의 Grid를 구해야하나?

### 백트랙킹
### 조합을 계산해야겠네
### 백 트랙킹으로 grid에서 돌 없애가면서 bfs

possible_grids = []

def bfs():
    from collections import deque
    
    visited = [[False] * n for _ in range(n)]
    directions = [(0,1), (0,-1), (1,0), (-1, 0)]
    queue = deque()
    count = 0
    for s_r, s_c in zip(r, c):

        queue.append((s_r, s_c))


        visited[s_r][s_c] = True
    
        count += 1

    while queue:
        c_r, c_c = queue.popleft()
        for d_r, d_c in directions:
            n_r, n_c = c_r+d_r, c_c+d_c

            if 0 <= n_r < n and 0 <= n_c < n:
                if grid[n_r][n_c] == 0:
                    if not visited[n_r][n_c]:
                        
                        visited[n_r][n_c] = True
                        queue.append((n_r, n_c))

                        count += 1

    return count

max_count = 0

def dfs(index, count):
    global max_count
    if count == m:
        # possible_grids.append([r[:] for r in grid])
        # possible_grids.append(grid.copy())

        ## 여기서 grid에서 bfs

        bfs_count = bfs() ########## 멀티소스 bfs
        max_count = max(bfs_count, max_count)

        return

    for i in range(index, n*n):
        g_r = i // n
        g_c = i % n

        if grid[g_r][g_c] == 1:
            grid[g_r][g_c] = 0
            dfs(i+1, count+1)
            grid[g_r][g_c] = 1
            



dfs(0,0)

print(max_count)