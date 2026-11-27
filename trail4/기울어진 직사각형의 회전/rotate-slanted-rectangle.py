n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())

# Please write your code here.

'''
시작점 주어짐.
    H, W 주어짐.
    H, W 만큼 밀기.
    반대 방향 순서로 밀면 됌. -> 반대방향 좌표가 애매함...
'''

r -= 1
c -= 1

new_grid = [row[:] for row in grid]

if dir == 0:

    direction = [
        (-1, 1),
        (-1, -1),
        (1, -1),
        (1, 1)
    ]

    hw = [m1,m2,m3,m4]

    temp = []
    
    for (dr, dc), count in zip(direction, hw):
        for _ in range(count):
            nr, nc = r+dr, c+dc

            new_grid[nr][nc] = grid[r][c]

            r, c = nr, nc

    grid = new_grid
    for row in grid:
        print(*row)

else:
    direction = [
        (-1, -1),
        (-1, 1),
        (1, 1),
        (1, -1)
    ]

    hw = [m2, m1, m4, m3]

    for (dr, dc), count in zip(direction, hw):
        for _ in range(count):
            nr, nc = r+dr, c+dc
            new_grid[nr][nc] = grid[r][c]

            r, c = nr, nc

    grid = new_grid
    for row in grid:
        print(*row)

