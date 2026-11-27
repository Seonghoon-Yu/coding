n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

# Please write your code here.

'''
M 개 이상 연속으로 같은 정수가 적혀 있는 폭탄은 터지고,
중력에 의해 밑으로 떨어짐.
'''




def exist(nums):
    possible = []

    if not nums:
        return possible

    count = 1
    prev = nums[0]



    for i in range(1, len(nums)):
        cur = nums[i]
        if cur != prev:
            if count >= m:
                possible.append((i-count, i-1))
            count = 1
        else:
            count += 1
        
        prev = cur

    if count >= m:
        possible.append(
            (len(nums) - count, len(nums) - 1)
        )
    
    return possible

# flag = True
while True:
    possible = exist(numbers)

    if not possible:
        break

    temp = numbers[:]
    for s, e in possible:
        for i in range(s, e+1):
            temp[i] = 0
    
    write = 0
    new_nums = []

    for i in range(len(temp)):
        if temp[i] !=0:
            new_nums.append(temp[i])
            # write += 1

    numbers = new_nums

count = 0
for n in numbers:
    if n != 0:
        count += 1

print(len(numbers))

for n in numbers:
    print(n)