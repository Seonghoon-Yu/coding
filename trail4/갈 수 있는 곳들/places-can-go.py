from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.


### Grid와 시작점 주어지고 각 시작지점으로부터 방문이 가능한 서로 다른 칸의 수 출력

directions = [(0,1), (0,-1), (1,0), (-1, 0)]

def bfs():
    queue = deque()

    for r, c in points:


        queue.append((r-1,c-1))
        visited[r-1][c-1] = True

    while queue:

        x, y = queue.popleft()

        ### 가능한 곳 찍먹
        for dx, dy in directions:
            nx, ny = x+dx, y+dy

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    if grid[nx][ny] == 0:
                        visited[nx][ny] += 1
                        queue.append((nx,ny))


visited = [[False] * n for _ in range(n)]

bfs()

count = 0
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            count += 1

print(count)