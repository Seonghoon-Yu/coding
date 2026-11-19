from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

# 상하좌우
directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]


def bfs():

    queue = deque()

    queue.append((0,0))
    visited[0][0] = True

    while queue:
        r, c = queue.popleft()

        if r == n-1 and c == m-1:
            return True

        for dr, dc in directions:
            nr, nc = r+dr, c+dc

            if 0<=nr<n and 0<=nc<m:
                if grid[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr,nc))


    return False

print(int(bfs()))












# def bfs(): ## bfs 선언

#     queue = deque() # deuqe 선언

#     # 시작 위치 넣기
#     queue.append((0, 0)) # 시작위치
#     visited[0][0] = True # 방문


#     # 큐에 갈 곳이 남아있는 동안 반복
#     while queue: # (0,0) 존재

#         # 가장 먼저 들어온 좌표 꺼내기
#         r, c = queue.popleft() # popleft


#         # 도착점에 도착했다면
#         if r == n - 1 and c == m - 1:
#             return 1


#         # 현재 위치에서 상하좌우 확인
#         for dr, dc in directions:

#             nr = r + dr
#             nc = c + dc


#             # 1. 격자 안이고
#             if 0 <= nr < n and 0 <= nc < m:

#                 # 2. 뱀이 없는 칸이고
#                 # 3. 아직 방문하지 않았다면
#                 if grid[nr][nc] == 1 and not visited[nr][nc]:

#                     # 방문 처리
#                     visited[nr][nc] = True

#                     # 앞으로 탐색할 곳에 추가
#                     queue.append((nr, nc))


#     # 큐가 다 비었는데 도착점을 못 만남
#     return 0


# print(bfs())