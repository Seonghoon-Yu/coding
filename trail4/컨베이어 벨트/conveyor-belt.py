n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.



## t 번 회전
## 1 번 회전 함수 작성


def rotate():
    temp_d = d[-1]
    temp_u = u[-1]

    for i in range(n-1, 0, -1):
        u[i] = u[i-1]

    u[0] = temp_d

    for j in range(n-1, 0, -1):
        d[j] = d[j-1]
    
    d[0] = temp_u


for _ in range(t):
    rotate()

print(*u)
print(*d)