n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


######## grid 에서 해당 좌표 찾기
### 해당 좌표에서 3가지 폭탄 탐색
### 터지는 좌표 저장
### set으로 겹치는 좌표 제거.
### 합이 최대로.


### dfs로 터지는 좌표 찾기
### 3가지 폭탄 넣어서 터지는 좌표.
### 다음 좌표, 폭탄 넣어서 터지는 좌표.
### 좌표들의 set



# ### 좌표는 완전 탐색으로 찾기
# for i in range(n):
#     for j in range(n):

block = [
    [(-1, 0), (-2, 0), (0,0), (1, 0), (2, 0)],
    [(-1, 0), (1, 0), (0,0), (0,-1), (0, 1)],
    [(1,1), (1,-1), (0,0), (-1,-1), (-1, 1)]
]


boomed = [[0] * n for _ in range(n)]



coords = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            coords.append((i,j))

max_value = 0

def dfs(index, boomed):
    global max_value

    if index == len(coords):
        summed = 0
        for b in boomed:
            summed += sum([x > 0 for x in b])
        max_value = max(max_value, summed)
        return
    
    coord = coords[index]
    cx, cy = coord

    for b in block:
        for dx, dy in b:
            if (0<= (cx+dx) < n) and (0<= (cy+dy) <n):
                boomed[cx+dx][cy+dy] += 1
            
        dfs(index+1, boomed)

        for dx, dy in b:
            if (0<= (cx+dx) < n) and (0<= (cy+dy) <n):
                boomed[cx+dx][cy+dy] -= 1            
        
dfs(0, boomed)

print(max_value)





# def dfs(index, count, total):
#     global answer, max_value
#     if count == len(coords):
#         answer = set()
#         for t in total:
#             for _ in t:
#                 answer.add(_)
        
#         max_value = max(max_value, len(answer))
#         return
    

#     coord = coords[index]
#     cx, cy = coord

#     for b in block:
#         boomed = set()
#         for (dx, dy) in b:
#             if (0 <= (cx + dx) < n) and (0 <= (cy + dy) < n):
#                 boomed.add((cx+dx, cy+dy))
#         total.append(boomed)
#         dfs(index+1, count+1, total)
#         total.pop()

# dfs(0,0,[])
# # print(answer)
# print(max_value)