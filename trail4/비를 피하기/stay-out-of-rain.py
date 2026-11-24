n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# 정수 0,1,2,3 으로만 이루어진 NxN 격자에서 사람 H명 겹치지 않고 서 있고 비를 피할 수 있는 공간의 위치 M개
# 각 사람마다 비를 피할 수 있는 가장 가까운 공간
# 0은 이동 가능, 1은 이동 X, 2는 서있을 수 있음, 3은 비 피할 수 있음.
# 한칸 움직이는데 1초
#
# 사람 있던 칸이 아니면 0
# 사람 있던 칸에 최소거리
# 비 피할 수 없으면 -1

# h명, m비 피하는 공간
# 우선 grid 에서 
## c_map 을 통해

## bfs 돌면서 m을 만나면 True
# 그 위치에서 가능횟수 저장
# 사람 위치 start, 도착 위치 m개

## 사람 위치 먼저 파악

start_point = []
end_point = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            start_point.append((i,j))
        if grid[i][j] == 3:
            end_point.append((i,j))


def bfs(r, c):
    from collections import deque

    block = [
        (1,0),
        (-1,0),
        (0,1),
        (0,-1)
    ]

    queue = deque()
    queue.append((r,c))

    visited[r][c] == True
    c_map[r][c] = 0

    possible = False
    while queue:
        r, c = queue.popleft()

        for dr, dc in block:
            nr, nc = r+dr, c+dc

            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] != 1:
                queue.append((nr, nc))
                visited[nr][nc] = True
                c_map[nr][nc] = c_map[r][c] + 1

                if (nr, nc) in end_point:
                    possible=True
        
        if possible:
            break


    return possible


answer = [[0] * n for _ in range(n)]

for r, c in start_point:
    visited = [[False] * n for _ in range(n)]
    c_map = [[0] * n for _ in range(n)]

    if bfs(r,c):

        min_count = float('inf')
        for r1, c1 in end_point:
            if visited[r1][c1]:
                # print(c_map)
                min_count = min(min_count, c_map[r1][c1])

        answer[r][c] = min_count
    else:
        answer[r][c] = -1

for row in answer:
    print(*row)







