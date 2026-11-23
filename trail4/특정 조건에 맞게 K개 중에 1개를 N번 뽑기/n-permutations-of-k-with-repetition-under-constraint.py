K, N = map(int, input().split())

# 1이상 K이하 정수. range 1,K)
# N번 반복해서 나올 수 있는 모든 서로다른 수열
# 연속하여 같은 정수가 3번 이상 나오는 경우 제외


def dfs(index, total):
    if len(total) == N:
        print(*total)
        return
    
    for i in range(1, K+1):
        
        #### 조건문
        if len(total) >= 2:
            prev_num = total[-1]
            pprev_num = total[-2]

            if not(prev_num == pprev_num == i):
                total.append(i)
                dfs(i+1, total)
                total.pop()



        else:
            total.append(i)
            dfs(i+1, total)
            total.pop()

dfs(0,[])