A = input()

# Please write your code here.


# 길이가 N인 문자열 A
# 오른쪽으로 순환 shift
# Run-Length Encoding 하여 결과 길이가 최소

# 오른쪽으로 K번 순환한다는거는 마지막 k문자를 순서 그래도 앞에 붙임.
# Run-Length encoding은 연속해서 나온 문자와 연속해서 나온 개수로 나타내는 방식

## K번 진행해서 최소 길이 구하기.
## 모든 K에 대해서 완전 탐색
# print(A)
temp = []
for _ in range(len(A)):
    temp.append(A[_])
# print(temp)

A=temp

min_length = 99
for _ in range(len(A)):
    last = A[-1]
    A[1:] = A[:-1]
    A[0] = last

    c_list = []
    count = 1
    c_list.append(A[0])
    for i in range(len(A)-1):
        cur_char = A[i]
        next_char = A[i+1]

        if cur_char == next_char:
            count += 1
        else:
            str_count = str(count)
            for count in str_count:
                c_list.append(count) 
            count = 1
            c_list.append(next_char)
    
    str_count = str(count)
    for count in str_count:
        c_list.append(count) 
    # c_list.append(count)
    length = len(c_list)
    min_length = min(min_length, length)
    # print(A)
    # print(c_list)

            
print(min_length)