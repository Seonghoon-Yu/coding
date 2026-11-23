n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())

r -= 1
c -= 1

# Please write your code here.
directions = [
    (-1, 1),
    (-1, -1),
    (1, -1),
    (1, 1)
]


new_grid = [row[:] for row in grid]

m = [m1, m2, m3, m4]


prev_r, prev_c = r, c

#### 0 (반시계)
#### 1 (시계)
if dir == 0:
    for (dr, dc), m in zip(directions, m):
        for _ in range(m):
            cr, cc = prev_r + dr, prev_c + dc
            # print(cr, cc)
            new_grid[cr][cc] = grid[prev_r][prev_c]            

            prev_r, prev_c = cr, cc

[2,1,4,3]

directions = [
    (-1, -1),
    (-1, 1),
    (1, 1),
    (1, -1)
]

m = [m2,m1,m4,m3]

if dir == 1:
    for (dr, dc), m in zip(directions, m):
        for _ in range(m):
            cr, cc = prev_r + dr, prev_c + dc
            # print(cr, cc)
            new_grid[cr][cc] = grid[prev_r][prev_c]            

            prev_r, prev_c = cr, cc


grid = new_grid
for row in grid:
    print(*row)


