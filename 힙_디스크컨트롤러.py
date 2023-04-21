import heapq

def solution(jobs):
    cnt,time,answer = 0,0,0
    len_jobs = len(jobs)
    heap = []

    while cnt<len_jobs:
        for job in jobs:
            if end<job[0]<=time:
                answer += time-job[0]
                heapq.heappush(heap, job[1])

        if heap:
            answer += len(heap)*heap[0]
            end = time
            time += heapq.heappop(heap)
            cnt += 1
        else:
            time +=1 

    return answer//3

print(solution([[0, 3], [1, 9], [2, 6]]))
