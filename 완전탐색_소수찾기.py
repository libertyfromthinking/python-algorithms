from itertools import permutations

def solution(numbers):
    s = set()
    for n in range(len(numbers)):
        s |= set(map(int,map(''.join,set(permutations(numbers,n+1)))))
    
    s -= set(range(0,2))
    s -= set(range(4,max(s)+1,2))
    
    for n in range(3,int(max(s)**0.5)+1,2):
        s -= set(range(n*2,max(s)+1,n))

    return len(s)

print(solution('011'))
