def solution(p, c):
    d = {}
    temp = 0

    for i in p:
        hash_value = hash(i)
        temp += hash_value
        d[hash_value] = i

    for i in c:
        hash_value = hash(i)
        temp -= hash_value

    return d[temp]
        
