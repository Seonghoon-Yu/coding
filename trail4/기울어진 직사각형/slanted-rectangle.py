n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

### 완전탐색
# 중심점 설멍.
# dx, dy 이동. max 이동
# 다음 가능한 dx, dy, max 이동
# 대각선 만든 다음에 합

block = [
    (-1, 1),
    (-1, -1),
    (1, -1),
    (1, 1)
]

def check_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False

max_value = 0

for i in range(n):

    for j in range(n):
        
        for w in range(1, n):
            for h in range(1, n):
                wh = [w, h, w, h]
                
                current_value = 0
                flag=True
                cx, cy = i, j
                    
                for b, k in zip(block, wh):
                    dx, dy = b
                    for _ in range(k):
                        
                        cx += dx
                        cy += dy

                        if check_range(cx, cy):
                            current_value += grid[cx][cy]
                            
                        else:
                            current_value = 0
                            flag = False

                if flag:
                    max_value = max(max_value, current_value)


print(max_value)
