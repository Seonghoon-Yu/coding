N = int(input())

# Please write your code here.

## 4가지 연산을 적절히 사용하여 연산의 횟수를 최소화 하여 1을 만들어냄.

### 현재수에서 1을 뻄
# 현재수에 1을 더함
# 현재수가 2로 나누어질 경우 2로 나눕
# 현재수가 3으로 나누어 떨어질 경우 3으로 나눔
# 11에서 시작하여 ..


##### dist 생성
dist = [0 for _ in range(N+4)]
visited = [False for _ in range(N+4)]

operation = [3,2,1,0]


def check_possible(commend, n):
    

    if commend == 1:
        if n+1 < N+3:
            return True
        return False
    
    if commend == 2:
        if n % 2 == 0:
            return True
        else:
            return False

    if commend == 3:
        if n % 3 == 0:
            return True
        else:
            return False
    
    return True


def operator(commend, n):
    if commend == 0:
        n -= 1
        return n
    
    if commend == 1:
        n += 1
        return n

    if commend == 2:
        n /= 2
        return int(n)
    
    if commend == 3:
        n /= 3
        return int(n)


def bfs():
    from collections import deque
    ######## 값을 ..
    ###### 더하는 연산 ..? 계속 더할수도 있잖아. visited 로 관리 해야겠네.

    queue = deque()
    queue.append(N)

    visited[N] = True

    while queue:
        n = queue.popleft()

        for o in operation:
            possible = check_possible(o, n)
            if possible:
                cn = operator(o, n)
                if not visited[cn]:
                    visited[cn] = True
                    queue.append(cn)
                    dist[cn] = dist[n] + 1
            else:
                continue
        
        if visited[1] == True:
            # print(visited)
            # print(dist)
            break
    
bfs()

print(dist[1])






    

