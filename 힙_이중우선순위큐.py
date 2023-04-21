import heapq

def solution(operations):
    heap = []

    for op in operations:
        operator, operand = op.split(' ')
        operand = int(operand)

        if operator=='I':
            heapq.heappush(heap, operand)
        elif heap:
            if operand<0:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))

    if not heap:
        return [0,0]

    return [max(heap), heapq.heappop(heap)]

print(solution(["I 7","I 5","I -5","D -1"]))
print(solution(["I 16","D 1"]))
