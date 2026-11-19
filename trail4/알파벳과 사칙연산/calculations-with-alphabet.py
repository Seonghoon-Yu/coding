expression = input()

# Please write your code here.

#### 알파벳 위치에 1,2,3,4 다 넣어보기.
#### 연산은 1, 3, 5 홀수 위치에 존재.

values = [0] * 6 # a b c d e f

answer = -float('inf')


def dfs(index):
    global answer

    if index == 6:
        ## 계산해보기
        results = calculate()

        answer = max(answer,results)
        return results

    ## 1부터 4까지 alphavet에 넣어보기
    for i in range(1, 5):
        values[index] = i
        dfs(index+1)

def calculate():
    ### 현재 value 값으로 연산 계산.

    cur_char = expression[0]
    cur_value = values[ord(cur_char)-ord('a')]

    
    for i in range(1, len(expression), 2):
        operator = expression[i]
        next_value = values[ord(expression[i+1])-ord('a')]
        if operator == "-":
            cur_value -= next_value
        
        if operator == "*":
            cur_value *= next_value

        if operator == '+':
            cur_value += next_value

    return cur_value



dfs(0)

print(answer)