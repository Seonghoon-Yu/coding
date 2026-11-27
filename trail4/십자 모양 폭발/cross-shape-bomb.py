n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.

'''
특정 위치 선택하면 그 위치를 중심으로 십자 모양 폭탄
크기는 선택된 위치에 있는 정수
터진 이후 중력에 의해 정수들이 떨어짐.
터진 얘들을 어떻게 옮겨오나 0 count 세서 0 이후 얘들 옮기기?
'''

r-=1
c-=1

## 폭탄 터트리기
temp = [row[:] for row in grid]


direction = [
    (1,0),
    (-1,0),
    (0, 1),
    (0, -1)
]


boom = grid[r][c]
temp[r][c] = 0

for dr, dc in direction:
    sr, sc = r, c

    for i in range(boom-1):
        nr, nc = sr+dr, sc+dc
        
        if 0<=nr<n and 0<=nc<n:
            temp[nr][nc] = 0

        sr, sc = nr, nc

# new_grid = [row[:] for row in temp]
new_grid = [[0] * n for _ in range(n)]

for c in range(n):
    white_r = n-1

    for r in range(n-1, -1, -1):

        if temp[r][c] != 0:
            new_grid[white_r][c] = temp[r][c]
            white_r -= 1


for row in new_grid:
    print(*row)



