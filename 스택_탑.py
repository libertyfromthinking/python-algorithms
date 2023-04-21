def solution(heights):
    answer = []

    for i in range(len(heights)-1, -1, -1):
        for j in range(i-1, -1, -1):
            if heights[i]<heights[j]:
                answer = [j+1]+answer
                break
        else:
            answer = [0]+answer
    return answer

print(solution([3,9,9,3,5,7,2]))
