from itertools import permutations

def solution(b):
    b_cmp = list(map(''.join,permutations('123456789',3)))
    len_b = len(b)
    
    for i in b:
        i[0] = str(i[0])
        for j in b_cmp[:]:
            st = 0
            for k in range(3):
                if i[0][k]==j[k]:
                    st += 1
            if i[1]!=st:
                b_cmp.remove(j)       
                continue
            if i[2]!=(len(set(i[0])&set(j))-st):
                b_cmp.remove(j)
                continue
    return len(b_cmp)

print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))
