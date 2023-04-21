def solution(begin, target, words):
    answer = 0 
    word_len = len(begin)
    begin = [begin]

    if not target in words:
        return 0

    while begin:
        temp = []
        for i in begin:
            for word in words:
                cnt = 0 
                for j in range(word_len):
                    if i[j] != word[j]:
                        cnt += 1
                    if cnt>1:
                        break
                if cnt==1:
                    temp.append(word)
                #words.remove(word)
        begin = temp
        answer += 1
        if target in begin:
            return answer
                        
    return answer

print(solution('hit', 'cog',["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution('hit', 'cog',["hot", "dot", "dog", "lot", "log"]))


