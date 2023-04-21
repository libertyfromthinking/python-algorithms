from collections import Counter

def solution(clothes):  
    clothe_dict = Counter([j for i,j in clothes])
    calc_num = 1
    
    for key in clothe_dict:
        calc_num *= clothe_dict[key]+1
    return calc_num-1
