# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input()

n = len(grid[0])
# Please write your code here.


## R -> 시계
## U -> 180
## L -> 반시계

# if dir == 'R':
    ## 시계
'''
1 2 3
4 5 6
7 8 9

7 4 1
8 5 2
9 6 3

00 -> 02
01 -> 12
02 -> 22

10 -> 01
11 -> 11
12 -> 21

'''

## 반시계
'''
1 2 3 
4 5 6
7 8 9

3 6 9
2 5 8
1 4 7
'''

def rotate(grid):
    new = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            new[c][n-r-1] = grid[r][c]

    return new

if dir == "R":
    grid = rotate(grid)
elif dir == "U":
    grid = rotate(grid)
    grid = rotate(grid)
elif dir == "L":
    grid = rotate(grid)
    grid = rotate(grid)
    grid = rotate(grid)
    

####### 이제 아래로 하는거 구현하면 됌.

def gravity(grid):

    new = [[0] * n for _ in range(n)]
    for c in range(n):
        write_r = n-1
        for r in range(n-1,-1,-1):   
            if grid[r][c] != 0:
                new[write_r][c] = grid[r][c]
                write_r -= 1 
    return new

def merge(grid):

    new = [[0] * n for _ in range(n)]
    merged = False

    grid = gravity(grid)

    for c in range(n):    
        # while merged:
        #     merged = False

        for r in range(n-2, -1, -1):

            ########## merge
            if grid[r][c] != 0 and grid[r][c] == grid[r+1][c]:
                grid[r+1][c] = grid[r][c] + grid[r+1][c]
                grid[r][c] = 0
                merged = True

    grid = gravity(grid)


    return grid


grid = merge(grid)
    

if dir == "R":
    grid = rotate(grid)
    grid = rotate(grid)
    grid = rotate(grid)
    
elif dir == "U":
    grid = rotate(grid)
    grid = rotate(grid)
elif dir == "L":
    grid = rotate(grid)
    
for row in grid:
    print(*row)