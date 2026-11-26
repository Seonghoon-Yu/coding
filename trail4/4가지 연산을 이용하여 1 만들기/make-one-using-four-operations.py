N = int(input())

# Please write your code here.
### dist를 따로 정의하는게 아니라 (N, 0) 으로 append

def bfs():
    from collections import deque
    queue = deque()
    queue.append((N, 0))

    visited = set()
    visited.add(N)

    while queue:
        n, count = queue.popleft()

        if n == 1:
            print(count)
            return
            
        next_nums = []

        next_nums.append(n-1)
        next_nums.append(n+1)

        if n % 2 == 0:
            next_nums.append(int(n//2))
        if n % 3 == 0:
            next_nums.append(int(n//3))

        for next in next_nums:
            if next not in visited:
                queue.append((next, count+1))
                visited.add(next)
        

bfs()



## 4가지 연산을 적절히 사용하여 연산의 횟수를 최소화 하여 1을 만들어냄.

### 현재수에서 1을 뻄
# 현재수에 1을 더함
# 현재수가 2로 나누어질 경우 2로 나눕
# 현재수가 3으로 나누어 떨어질 경우 3으로 나눔
# 11에서 시작하여 ..

# from collections import deque

# N = int(input())


# def bfs():

#     # 큐에는
#     # (현재 숫자, 현재까지 연산 횟수)
#     q = deque()
#     q.append((N, 0))

#     # +1 연산이 있기 때문에
#     # 이미 방문했던 숫자로 다시 돌아갈 수 있음.
#     #
#     # 예)
#     # 10 -> 11 -> 10 -> 11 ...
#     #
#     # 따라서 방문 체크 필요
#     visited = set()
#     visited.add(N)


#     while q:

#         cur, count = q.popleft()


#         # =========================
#         # 1에 처음 도착
#         # =========================
#         #
#         # BFS이므로 처음 도착한 순간이
#         # 최소 연산 횟수
#         if cur == 1:
#             return count


#         # =========================
#         # 다음에 갈 수 있는 숫자
#         # =========================

#         next_nums = []


#         # 1. 현재 수에서 1 빼기
#         next_nums.append(cur - 1)


#         # 2. 현재 수에서 1 더하기
#         next_nums.append(cur + 1)


#         # 3. 2로 나누어 떨어지면
#         #    2로 나누기
#         if cur % 2 == 0:
#             next_nums.append(cur // 2)


#         # 4. 3으로 나누어 떨어지면
#         #    3으로 나누기
#         if cur % 3 == 0:
#             next_nums.append(cur // 3)


#         # =========================
#         # 다음 숫자 BFS에 추가
#         # =========================
#         for nxt in next_nums:

#             # 이미 방문한 숫자는 다시 볼 필요 없음
#             if nxt not in visited:

#                 visited.add(nxt)

#                 q.append(
#                     (nxt, count + 1)
#                 )


# print(bfs())



# ##### dist 생성
# dist = [0 for _ in range(N+4)]
# visited = [False for _ in range(N+4)]

# operation = [3,2,1,0]


# def check_possible(commend, n):
    

#     if commend == 1:
#         if n+1 < N+3:
#             return True
#         return False
    
#     if commend == 2:
#         if n % 2 == 0:
#             return True
#         else:
#             return False

#     if commend == 3:
#         if n % 3 == 0:
#             return True
#         else:
#             return False
    
#     return True


# def operator(commend, n):
#     if commend == 0:
#         n -= 1
#         return n
    
#     if commend == 1:
#         n += 1
#         return n

#     if commend == 2:
#         n /= 2
#         return int(n)
    
#     if commend == 3:
#         n /= 3
#         return int(n)


# def bfs():
#     from collections import deque
#     ######## 값을 ..
#     ###### 더하는 연산 ..? 계속 더할수도 있잖아. visited 로 관리 해야겠네.

#     queue = deque()
#     queue.append(N)

#     visited[N] = True

#     while queue:
#         n = queue.popleft()

#         for o in operation:
#             possible = check_possible(o, n)
#             if possible:
#                 cn = operator(o, n)
#                 if not visited[cn]:
#                     visited[cn] = True
#                     queue.append(cn)
#                     dist[cn] = dist[n] + 1
#             else:
#                 continue
        
#         if visited[1] == True:
#             # print(visited)
#             # print(dist)
#             break
    
# bfs()

# print(dist[1])






    

