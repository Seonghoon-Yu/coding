n = int(input())
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

# Please write your code here.


### 모든 가능한 조합
### line들의 overlab check

max_value = 0

def dfs(index, total):
    global max_value
    if index > n:
        return

    if total:
        ## 정렬
        possible=True
        sorted_total = sorted(total, key=lambda x: (x[1], x[0])) # 끝점이 작은 순

        ## 조합 내의 선들 완전 탐색
        for i in range(len(total)):
            for j in range(i+1, len(total)):
                a,b = cur_line = sorted_total[i]
                c,d = next_line = sorted_total[j]

                if not (b < c): ## 겹침
                    possible=False
                    break

            if possible==False:
                break
        
        if possible:
            max_value = max(max_value, len(total))
            


    ## 가능한 조합
    for i in range(index, n):
        line = (x1[i], x2[i])
        total.append(line)
        dfs(i+1, total)
        total.pop()


dfs(0,[])
print(max_value)






# def dfs(index, total):
#     global max_value
#     if index > n:
#         # print(total)
#         return
    
#     ## check를 여기에
#     ###### 겹쳤는지, 안겹쳤는지는 완전 탐색으로 모두 조합해서 check 하기.

#     possible = True
#     if total:
#         ## 정렬
#         # total = total.sort(key=lambda x: (x[1], x[0]))
        
#         sorted_total = sorted(total, key=lambda x: (x[1], x[0]))
#         for i in range(len(total)):
#             for j in range(i+1, len(total)): # 1개일때 자동으로 검사 안함.
#                 a, b = total[i]
#                 c, d = total[j]

#                 if not ((b < c) or (d < a)): ## 겹치는 부분
#                     possible = False
#                     break
            
#             if not possible:
#                 break

        
#         if possible:      
#             max_value = max(max_value, len(total))



#     ## 다음
#     for i in range(index,n):
#         line = (x1[i], x2[i])
#         total.append(line)
#         dfs(i+1, total)
#         total.pop()

# dfs(0, [])

# print(max_value)