n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


count_map = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

## bfs

## 넘어갈때마다 count


def bfs():
    from collections import deque

    block = [
        (1,0),
        (-1,0),
        (0,-1),
        (0,1)
    ]


    queue = deque()
    queue.append((0,0))

    visited[0][0] = True


    while queue:
        r, c = queue.popleft()

        for dr, dc in block:
            nr, nc = r+dr, c+dc

            if 0<=nr<n and 0<=nc<m and not visited[nr][nc] and grid[nr][nc] == 1:
                queue.append((nr, nc))
                visited[nr][nc] = True
                if count_map[nr][nc] < count_map[r][c] + 1:
                    count_map[nr][nc] = count_map[r][c] + 1

bfs()
# print(count_map)
if count_map[n-1][m-1] == 0:
    print(-1)
else:
    print(count_map[n-1][m-1])



