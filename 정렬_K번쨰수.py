def solution(array, commands):
    answer = []
    print(array)
    for arr in commands:
        v = array[(arr[0]-1):arr[1]]
        v.sort()
        answer.append(v[arr[2]-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
