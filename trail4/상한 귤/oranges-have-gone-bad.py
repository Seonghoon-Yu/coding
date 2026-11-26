n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

## K개의 상한귤
# 1초마다 상하좌우 귤이 상함.
# 각 귤마다 최초로 상하게 되는 시간
# 0 no, 1 귤, 2 상한귤

##### 상한귤 위치 찾아서 거기서부터 multi-source bfs
## 상한귤 인접. 끝까지 상하지 않는 귤이라면 -2

damaged = []
mandarin = []

dist = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            damaged.append((i,j))
        if grid[i][j] == 0:
            dist[i][j] = -1
        if grid[i][j] == 1:
            mandarin.append((i,j))


def bfs():
    from collections import deque


    queue = deque()
    for dr, dc in damaged:
        queue.append((dr, dc))
        visited[dr][dc] = True
        dist[dr][dc] = 0

    while queue:
        r, c = queue.popleft()

        for dr, dc in block:
            nr, nc = r+dr, c+dc

            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True

                if grid[nr][nc] == 0:
                    dist[nr][nc] = -1
                if grid[nr][nc] == 1:
                    grid[nr][nc] = -1
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr,nc))
        
block = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)
]

visited = [[False] * n for _ in range(n)]


bfs()

for mr, mc in mandarin:
    if dist[mr][mc] == 0:
        dist[mr][mc] = -2


for d in dist:
    print(*d)