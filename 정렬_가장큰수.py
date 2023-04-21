def solution(numbers):
    numbers = list(map(str,numbers))
    numbers = sorted(numbers, key=lambda x:x*3, reverse=True)
    return ''.join(numbers)

print(solution([3,30,34,5,9]))
