from collections import deque

def solution(bridge_len, weight, truck_weights):
    second = 0
    q = deque([0]*bridge_len)
    truck_weights = deque(truck_weights)
    q_sum = 0

    while q:
        q_sum -= q.popleft()
        second += 1

        if truck_weights:
            if truck_weights[0]+q_sum<=weight:
                q_sum += truck_weights[0]
                q.append(truck_weights.popleft())
            else:
                q.append(0)
    
    return second

print(solution(2, 10, [7,4,5,6]))
