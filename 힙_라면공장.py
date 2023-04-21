from heapq import *

def solution(stock, dates, supplies, k):
    answer = 0
    start = 0
    date_len = len(dates)
    heap = []

    while stock<k:
        for i in range(start, date_len):
            if dates[i]<=stock:
                heappush(heap, -supplies[i])
                start += 1
            else:
                break
        answer += 1
        stock += -heappop(heap)

    return answer

print(solution(4, [4,10,15], [20,5,10], 30))

