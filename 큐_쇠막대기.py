from collections import deque

def solution(arr):
    answer = 0
    stick = 0
    q = deque(arr)

    while q:
        val = q.popleft()
        if val=='(' and q[0]==')':
            q.popleft()
            answer += stick
        elif val=='(':
            stick += 1
            answer += 1
        else:
            stick -= 1

    return answer

print(solution("()(((()())(())()))(())"))
        

