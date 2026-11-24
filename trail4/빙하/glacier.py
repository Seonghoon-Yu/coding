n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

## N x M 크기 격자안 빙하의 정보.
# 격자 가장 바깥은 항상 빙하가 아니고, 빙하를 제외한 부분은 물이 채워져있음.
# 정수 1은 빙하, 0은 물

# 바깥물 인접한 모든 빙하 칸을 동시에 녹임

# 빙하가 전부 녹는데 걸리는 식ㄴ, 마지막 초에 녹아 사라지는 빙하 칸의 수

# 바깥물을 bfs로 update # update 해가면서 인접된 물 녹이기
# 이전 state 저장해두고, 다 녹았을시 꺼내서 씀


def bfs():
    from collections import deque

    block = [
        (1,0),
        (-1,0),
        (0,1),
        (0,-1)
    ]

    queue = deque()
    queue.append((0,0))

    visited[0][0] = True

    while queue:
        r, c = queue.popleft()

        for dr, dc in block:
            nr, nc = r+dr, c+dc

            if 0<=nr<n and 0<=nc<m and not visited[nr][nc]:
                if grid[nr][nc] == 0:
                    queue.append((nr,nc))
                    visited[nr][nc] = True
                elif grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    visited[nr][nc] = True
    





prev_grid = [row[:] for row in grid]
prev_count = sum([sum(row) for row in grid])

for t in range(1, 100):

    visited = [[False] * m for _ in range(n)]    
    

    bfs()
    
    # prev_grid = [row[:] for row in grid]

    count = sum([sum(row) for row in grid])
    # print(count)
    if count == 0:
        break

    prev_count = count

print(t, prev_count)



