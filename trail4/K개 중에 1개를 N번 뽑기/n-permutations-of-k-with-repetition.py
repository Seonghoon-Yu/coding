K, N = map(int, input().split())

# Please write your code here.

def dfs(total, count):
    if count == N:
        print(*total)
        return

    
    for i in range(1, K+1):
        total.append(i)
        dfs(total, count+1)
        total.pop()
    
dfs([], 0)

