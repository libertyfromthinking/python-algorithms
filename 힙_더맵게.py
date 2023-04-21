from heapq import *

def solution(scoville, K):
    heapify(scoville)
    cnt = 0

    while scoville[0]<K:
        cnt += 1
        try:
            heappush(scoville, heappop(scoville)+heappop(scoville)*2)
        except:
            return -1

    return cnt

print(solution([3, 1,2, 9, 10, 12],7))
