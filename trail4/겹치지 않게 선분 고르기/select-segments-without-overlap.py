n = int(input())
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

# Please write your code here.


#### N 개로 가능한 모든 순열 -> dfs
# 1개 고르기, 두개 고르기, 세개 고르기 어떻게?
# 종료 조건이 확실하지 않음.
# 
#### 겹쳤는지 안겹쳤는지 확인

max_value = 0
def dfs(index, total):
    global max_value
    if index > n:
        # print(total)
        return
    
    ## check를 여기에
    ###### 겹쳤는지, 안겹쳤는지는 완전 탐색으로 모두 조합해서 check 하기.

    possible = True
    if total:
        for i in range(len(total)):
            for j in range(i+1, len(total)): # 1개일때 자동으로 검사 안함.
                a, b = total[i]
                c, d = total[j]

                if not ((b < c) or (d < a)): ## 겹치는 부분
                    possible = False

        
        if possible:      
            max_value = max(max_value, len(total))



    ## 다음
    for i in range(index,n):
        line = (x1[i], x2[i])
        total.append(line)
        dfs(i+1, total)
        total.pop()

dfs(0, [])

print(max_value)