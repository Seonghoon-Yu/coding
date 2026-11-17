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

max_sum = 0

dy = [1, -1, -1, 1]
dx = [-1, -1, 1, 1]

###### 좌표에서 h, w 가능한 마름모 그려보기
#### 해당 좌표에서 가능한 h, w 계산
#### 해당 h, w 마름모를 그릴 수 있는지 check
### 그릴 수 있으면 계산

for i in range(n):
    for j in range(n):


        # ### 모든 가능한 h, w 조합


        for h in range(1, n):
            for w in range(1, n):
                length = [h, w, h, w]
                
                cx, cy = i, j

                current_sum = 0
                possible = True
                for d in range(4): ## 4개 이동 좌표
                    for _ in range(length[d]):
                        cx += dx[d]
                        cy += dy[d]
                        
                        if (0 <= cx < n) and (0 <= cy < n):
                            current_sum += grid[cx][cy]
                        else:
                            possible = False
                            break
                    
                    if not possible:
                        break
                
                if possible:
                    max_sum = max(max_sum, current_sum)

print(max_sum)



# for i in range(n):
#     for j in range(n):

#         for w in range(1, n):
#             for h in range(1, n):
#                 wh = [w, h, w, h]
#                 cx, cy = i, j

#                 current_sum = 0
#                 possible = True
                
#                 # current_sum += grid[i][j]

#                 for b, length in zip(block, wh):
#                     dx, dy = b
#                     for _ in range(length):
#                         cx += dx
#                         cy += dy
#                         if check_range(cx, cy):
#                             current_sum += grid[cx][cy]
#                         else:
#                             possible=False
                            
                
#                 if possible:
#                     max_value = max(max_value, current_sum)

# print(max_value)
