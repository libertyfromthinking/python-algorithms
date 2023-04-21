def solution(b, r):
    for i in range(1,int(r**0.5)+1):
        if r%i==0:
            if ((r//i+i)*2+4)==b:
                return [r//i+2,i+2]

print(solution(24,24))
