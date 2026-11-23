n, m, q = map(int, input().split())

# Create 2D array for building state
a = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.


## 정수들을 시계방향으로 shift
## 해당 직사각형 내 있는 값들을 자신 위치 기준으로 인접한 원소들과 평균값. 버림.
## 인접한 값들은 상하 좌우.

### 1. 직사각형 shift (경계만.)
### 2. 각 요소에서 인접 요소 평균

## 우선 경계만 하는 법.
## 경계 훑는법.

## r1, c1, 좌측 상단
## r2, c2 우측 하단

def rotate(r1, c1, r2, c2):
    r1_temp = a[r1][c2]    
    c2_temp = a[r2][c2]
    r2_temp = a[r2][c1]
    c1_temp = a[r1][c1]


    # -> 
    for i in range(c2, c1, -1):
        a[r1][i] = a[r1][i-1]
    a[r1][c1] = c1_temp

    # v
    for i in range(r2, r1, -1):
        a[i][c2] = a[i-1][c2]

    a[r1+1][c2] = r1_temp

    # <-
    for i in range(c1, c2):
        a[r2][i] = a[r2][i+1]
    
    a[r2][c2-1] = c2_temp

    # ^
    for i in range(r1,r2):
        a[i][c1] = a[i+1][c1]
    
    a[r2-1][c1] = r2_temp


def fill_element(r1, c1, r2, c2):
    direction = [(0,1), (0,-1), (1,0), (-1, 0)]
    
    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            elements = []
            elements.append(a[r][c])

            for dr, dc in direction:
                if 0 <= r+dr < n and 0 <= c+dc < m:
                    elements.append(a[r+dr][c+dc])

            e = sum(elements) // len(elements)

            new_grid[r][c] = e

                





for r1, c1, r2, c2 in winds:
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1

    rotate(r1,c1,r2,c2)
    new_grid = [row[:] for row in a]
    fill_element(r1,c1,r2,c2)
    a = new_grid

for row in a:
    print(*row)
