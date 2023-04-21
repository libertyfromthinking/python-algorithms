def solution(answers):
    m1 = [1, 2, 3, 4, 5]
    m2 = [2, 1, 2, 3, 2, 4, 2, 5]
    m3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    len_m1 = len(m1)
    len_m2 = len(m2)
    len_m3 = len(m3)
    score = [0,0,0]
    result = []

    for i in range(len(answers)):
        if answers[i]==m1[i%len_m1]:
            score[0] += 1
        if answers[i]==m2[i%len_m2]:
            score[1] += 1
        if answers[i]==m3[i%len_m3]:
            score[2] += 1

    max_score = max(score)
    
    for i in range(1,4):
        if score[i-1]==max_score:
            result.append(i)

    return result


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
