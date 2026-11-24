n = int(input())
r1, c1, r2, c2 = map(int, input().split())

# Please write your code here.



c_map = [[0]* n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def bfs(r1, c1):
    from collections import deque
    
    block = [
        (-2, 1),
        (-1, 2),
        (1, 2),
        (2, 1),
        (2, -1),
        (1, -2),
        (-1, -2),
        (-2, -1)
    ]
    
    queue = deque()
    queue.append((r1, c1))

    visited[r1][c1] = True

    while queue:
        r, c = queue.popleft()

        for dr, dc in block:
            nr, nc = r+dr, c+dc

            if 0<=nr<n and 0<=nc<n and not visited[nr][nc]:
                queue.append((nr,nc))
                visited[nr][nc]=True
                c_map[nr][nc] = c_map[r][c] + 1


bfs(r1-1,c1-1)


if visited[r2-1][c2-1]:
    print(c_map[r2-1][c2-1])
else:
    print(-1)



