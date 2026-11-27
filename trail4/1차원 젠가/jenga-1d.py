n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.

'''
1차원 젠가
각 층마다 1개의 블록, 각 블록에는 정수가 하나씩.
2번에 걸쳐 특정 구간의 블록들을 뺴는 작업
특정 구간의 블록을 두번 쨰는 과정을 거친 후 이후의 결과
'''


## temp 저장. -> update -> 

s1 -= 1
e1 -= 1
s2 -= 1
e2 -= 1

def remove(s, e):
    temp = []

    count = 0
    for b in blocks:

        if not(s <= count <= e):
            temp.append(b)

        count += 1

    return temp


blocks = remove(s1, e1)
blocks = remove(s2, e2)

print(len(blocks))
for b in blocks:
    print(b)