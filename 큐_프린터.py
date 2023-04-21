from collections import deque

def solution(priorities, location):
    queue = deque([[i,j]for i,j in enumerate(priorities)])
    answer = 0

    while queue:
        val = queue.popleft()
        if any([val[1]<i[1] for i in queue]):
            queue.append(val)
        else:
            answer += 1
            if val[0]==location:
                return answer

print(solution([1,1,9,1,1,1],0))
        
