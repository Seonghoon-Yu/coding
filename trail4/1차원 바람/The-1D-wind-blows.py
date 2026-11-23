n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

# Please write your code here.

## right rotate 함수
## left rotate 함수
## 바람
## 전파 check
## 전파이면 rotate


def l_rotate(r):
    
    a_temp = a[r][-1]
    for i in range(m-1, 0, -1):
        a[r][i] = a[r][i-1]

    a[r][0] = a_temp

def r_rotate(r):
    a_temp = a[r][0]

    for i in range(0,m-1):
        a[r][i] = a[r][i+1]
    
    a[r][-1] = a_temp

def prop(r, wind_d):
    u_possible = False
    d_possible = False

    prev_u = r
    prev_d = r

    prev_u_d = wind_d
    prev_d_d = wind_d

    ### 위에 행 check
    while prev_u > 0:
        u_possible = False
        ## 전파가 되는지 확인
        next_u = prev_u -1
        for i in range(m):
            if a[prev_u][i] == a[next_u][i]:
                u_possible = True
            
        if not u_possible:
            break
        
        if u_possible:
            if prev_u_d == 'L':
                r_rotate(next_u)
                prev_u_d = 'R'
            elif prev_u_d == 'R':
                l_rotate(next_u)
                prev_u_d = 'L'
        
        prev_u = next_u

    while prev_d < n-1:
        d_possible = False

        next_d = prev_d + 1
        for i in range(m):
            if a[prev_d][i] == a[next_d][i]:
                d_possible = True
        
        if not d_possible:
            break
        
        if d_possible:
            if prev_d_d == 'L':
                r_rotate(next_d)
                prev_d_d = 'R'
            elif prev_d_d == 'R':
                l_rotate(next_d)
                prev_d_d = 'L'
        
        prev_d = next_d
    

                







for r, d in winds:
    r -= 1
    if d == 'L':
        l_rotate(r)
    if d == 'R':
        r_rotate(r)

    ## 전파 확인
    prop(r, d)


for r in a:
    print(*r)    


