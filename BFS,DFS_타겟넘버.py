from itertools import product

def solution(numbers, target):
    numbers = [(i,-i) for i in numbers]
    result = list(map(sum,product(*numbers)))
    return result.count(target)

print(solution([1,1,1,1,1],3))
