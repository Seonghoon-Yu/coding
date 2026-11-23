n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.


def rotate():
    temp_l = l[-1]
    temp_r = r[-1]
    temp_d = d[-1]

    for i in range(n-1, 0, -1):
        l[i] = l[i-1]
        r[i] = r[i-1]
        d[i] = d[i-1]
    
    l[0] = temp_d
    r[0] = temp_l
    d[0] = temp_r

for _ in range(t):
    rotate()


print(*l)
print(*r)
print(*d)